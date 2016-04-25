# indi-weewx
WeeWX UDP extension and corresponding INDI interface

## Description
This driver is a WeeWX extension (*inspired by the csv service*) generating UDP
packets on LOOP packets/archive record reception and the corresponding INDI
Weather driver.

We use UDP because it's "fire and forget", WeeWX doesn't need to keep track of
clients state/connections and there is no need to have anybody listening
(clients can came and go).

We try to be compatible with Meteo software because it's supported/used by
RTS2, an integrated solution for remote observatory control (but WeeWX is able
to get data from more sources/weather stations).

## Configuration options
* WeeWX extension:
  * binding (LOOP packet or archive record)
  * source ip (?)
  * destination port
  * transmission type (unicast/multicast/broadcast, multicast *could* require
    advanced routing configuration, broadcast *requires* the sender and the
    receiver to be on the same network segment)
  * format (meteo-compatible/json)
* INDI driver:
  * local ip to bind on (0.0.0.0 or something else if you have advanced needs)
  * port
  * format (could be automatically recognized?)
  * timeout (should be at least 3 times the packet frequency)

## TODO
* could this work for non-Davis weather stations? (at least the simulator)
  * http://www.weewx.com/docs/customizing.htm says: "LOOP packets may or may
    not contain all the data types. For example, a packet may contain only
    temperature data, another only barometric data, etc.. This kind of packet
    is called a partial record packet. For other types of hardware (notably the
    Vantage series), every LOOP packet contains every data type."
* test with Meteo (RTS2 should be fine with WeeWX-originated data and INDI
  should be fine with Meteo packets)
* licensing: TBD (should be compatible with WeeWX and INDI)
* security (source/data authentication, avoiding that someone evil on your
  network could shut down your observatory)
* ipv6

## Link
* https://github.com/weewx/weewx/wiki/csv
* http://lancet.mit.edu/mwall/projects/weather/releases/
* http://meteo.othello.ch/
* http://rts2.org/wiki/doku.php?id=howto:intergation_of_a_davis_meteo_station
* http://www.indilib.org/api/classINDI_1_1Weather.html
