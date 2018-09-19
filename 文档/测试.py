# # < style
# # type = "text/css" >
# # .banner
# # {
# #     position: relative;
# # overflow: auto;
# # text - align: center;
# # }
# # .banner
# # ul
# # li
# # {
# #     list - style: none;
# # float: left;
# # }
# # # banner {
# # width: 100 %;
# # height: 500
# # px;
# # }
# # # banner .dots {
# # position: absolute;
# # left: 0;
# # right: 0;
# # bottom: 20
# # px;
# # }
# # # banner .dots li {
# # display: inline - block;
# # width: 10
# # px;
# # height: 10
# # px;
# # margin: 0
# # 4
# # px;
# # text - indent: -999
# # em;
# # border: 2
# # px
# # solid  # fff;
# # border - radius: 6
# # px;
# # cursor: pointer;
# # opacity: .4;
# # -webkit - transition: background
# # .5
# # s, opacity
# # .5
# # s;
# # -moz - transition: background
# # .5
# # s, opacity
# # .5
# # s;
# # transition: background
# # .5
# # s, opacity
# # .5
# # s;
# # }
# # # banner .dots li.active {
# # background:  # fff;
# # opacity: 1;
# # }
# # # banner .arrow {
# # position: absolute;
# # top: 200
# # px;
# # }
# # # banner #al {
# # left: 15
# # px;
# # }
# # # banner #ar {
# # right: 15
# # px;
# # }
# # # banner img {
# # width: 100 %;
# # height: 500
# # px;
# # }
# # < / style >
# { %
# for category in categories %}
# < div >
# < span
#
#
# class ="glyphicon glyphicon-grain cate" > < / span > < a href="#" > {{category.name}} < / a >
#
# < ul
#
#
# class ="sub" >
#
#
# { %
# for sub in category.subs %}
# < div
# id = "sub_menu1" >
# < span
# id = "cate_sub" > < span > {{sub.name}} < / span > < span
#
#
# class ="glyphicon glyphicon-menu-right" > < / span > < / span >
#
# < / div >
# < br >
# < div
# id = 'sub_menu2' >
# { %
# for sub2 in sub.subs2 %}
# < span
# id = "cate_sub2" > < a
# href = "#" > {{sub2.name}} < / a > < / span >
#
# { % endfor %}
# < / div >
# < br >
# { % endfor %}
# < / ul >
# < / div >
# { % endfor %}