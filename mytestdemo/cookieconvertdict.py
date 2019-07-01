import json

"""
    将原生的 cookie 字符串抓换为字典
"""
# cookie = "wb_view_log=1536*8641.25; SINAGLOBAL=403930036070.79645.1561443728699; wb_view_log_6257491595=1536*8641.25; UOR=,,login.sina.com.cn; un=13436417800; wb_timefeed_6257491595=1; Ugrow-G0=1ac418838b431e81ff2d99457147068c; YF-V5-G0=f0aa2e6d566ccd1c288fae19df01df56; _s_tentry=login.sina.com.cn; Apache=4986170472530.434.1561449051519; ULV=1561449051530:3:3:3:4986170472530.434.1561449051519:1561448474488; cross_origin_proto=SSL; YF-Page-G0=6affec4206bb6dbb51f160196beb73f2|1561450951|1561450951; webim_unReadCount=%7B%22time%22%3A1561450964532%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; login_sid_t=8b5346755079f5e4d49fff5eb41dcb90; WBStorage=6b696629409558bc|undefined; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5WavXZSGh-flM42rmNd2CH5JpX5K2hUgL.FoqESKMX1K2f1K-2dJLoIEy_Ig4Di--Ri-i8i-20i--fiK.0i-2ci--Ri-zXiKL2i--Ri-zXiKL2; ALF=1592987030; SSOLoginState=1561451032; SCF=Akr9hguT2JWcdhKSTRaClyatnlQEwrE3E4oDA7QOKf-NwN73m_IRA6dYwP-1hL3glol5we0i_6CLTkAPcxZX71s.; SUB=_2A25wFapIDeRhGeBM7lUV-S_JwjmIHXVTYpyArDV8PUNbmtBeLUTukW9NRK0U50pc1wL6mr61yXKb4LxvU17fyqtH; SUHB=0sqBuHP9CKBUZh; wvr=6"
cookie = "_T_WM=c2f229efc05784054394e41b6445a61b; SCF=Akr9hguT2JWcdhKSTRaClyatnlQEwrE3E4oDA7QOKf-NATrmqcIO4GhB2IpGQz1PSyYsBz3vjlbFvHNjyYqnkjM.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5WavXZSGh-flM42rmNd2CH5JpX5K-hUgL.FoqESKMX1K2f1K-2dJLoIEy_Ig4Di--Ri-i8i-20i--fiK.0i-2ci--Ri-zXiKL2i--Ri-zXiKL2; SUB=_2A25wFZYnDeRhGeBM7lUV-S_JwjmIHXVT-TpvrDV6PUJbkdAKLRjzkW1NRK0U5yeV4tuMWa7YXXy-0hn7udgaGXWO; SUHB=03oFH9YAaoobvM; SSOLoginState=1561454198"
cookiekey = []
cookievalue = []
cookies = cookie.split("; ")
for co in cookies:
    co = co.strip()
    p = co.split('=')
    cookiekey.append(p[0])
    cookievalue.append(p[1])

cookieDict = dict(zip(cookiekey, cookievalue))
print(cookieDict)
