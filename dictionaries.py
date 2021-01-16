#   special structure which stores value with its key
#   key should be unique
#   values can be repeated
#
monthsConversions ={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    12:"December",
}
# accessing key value
print(monthsConversions[12])
print(monthsConversions.get("Jun"))
# if key is not present then it prints "None"
# you can make key of number type (integer)
print(monthsConversions.get("ew","Not Valid key"))




