# Copyright 2016 Riccardo Stagni

import syslog

import weewx
import weewx.engine
import weeutil.weeutil

class UDP(weewx.engine.StdService):
    def __init__(self, engine, config_dict):
        super(UDP, self).__init__(engine, config_dict)
        d = config_dict.get('UDP', {})
        self.port = d.get('port', '42666')
#        self.header = weeutil.weeutil.tobool(d.get('header', True))
#        self.mode = d.get('mode', 'append')
        self.binding = d.get('binding', 'loop')
        if self.binding == 'loop':
            self.bind(weewx.NEW_LOOP_PACKET, self.handle_new_loop)
        else:
            self.bind(weewx.NEW_ARCHIVE_RECORD, self.handle_new_archive)

    def handle_new_loop(self, event):
        self.write_data(event.packet)

    def handle_new_archive(self, event):
        self.write_data(event.record)

    def write_data(self, data):
        syslog.syslog(syslog.LOG_INFO, "UDP: keys %s" % ','.join(self.sort_keys(data)))
        syslog.syslog(syslog.LOG_INFO, "UDP: data %s" % ','.join(self.sort_data(data)))

    def sort_keys(self, record):
        fields = ['dateTime']
        for k in sorted(record):
            if k != 'dateTime':
                fields.append(k)
        return fields

    def sort_data(self, record):
        fields = [str(record['dateTime'])]
        for k in sorted(record):
            if k != 'dateTime':
                fields.append(str(record[k]))
        return fields
