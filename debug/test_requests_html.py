from requests_html import HTMLSession

from fake_useragent import UserAgent


ua = UserAgent(browsers=["chrome"])

headers = {
    "user-agent": ua.random,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6,ja;q=0.5",
    "cache-control": "no-cache",
    "origin": "https://www.unitedstateszipcodes.org",
    "dnt": "1",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    # "cookie": "from_zip=a%3A33%3A%7Bs%3A7%3A%22quality%22%3Bs%3A2%3A%2260%22%3Bs%3A8%3A%22latitude%22%3Bs%3A9%3A%2238.935776%22%3Bs%3A9%3A%22longitude%22%3Bs%3A10%3A%22-77.159523%22%3Bs%3A9%3A%22offsetlat%22%3Bs%3A9%3A%2238.935848%22%3Bs%3A9%3A%22offsetlon%22%3Bs%3A9%3A%22-77.16214%22%3Bs%3A6%3A%22radius%22%3Bs%3A4%3A%224800%22%3Bs%3A11%3A%22boundingbox%22%3Ba%3A4%3A%7Bs%3A5%3A%22north%22%3Bs%3A8%3A%2238.96841%22%3Bs%3A5%3A%22south%22%3Bs%3A9%3A%2238.903141%22%3Bs%3A4%3A%22east%22%3Bs%3A10%3A%22-77.116539%22%3Bs%3A4%3A%22west%22%3Bs%3A10%3A%22-77.202507%22%3B%7Ds%3A4%3A%22name%22%3BN%3Bs%3A5%3A%22line1%22%3BN%3Bs%3A5%3A%22line2%22%3Bs%3A16%3A%22Mclean%2C+VA+22101%22%3Bs%3A5%3A%22line3%22%3BN%3Bs%3A5%3A%22line4%22%3Bs%3A13%3A%22United+States%22%3Bs%3A5%3A%22cross%22%3BN%3Bs%3A5%3A%22house%22%3BN%3Bs%3A6%3A%22street%22%3BN%3Bs%3A7%3A%22xstreet%22%3BN%3Bs%3A8%3A%22unittype%22%3BN%3Bs%3A4%3A%22unit%22%3BN%3Bs%3A6%3A%22postal%22%3Bs%3A5%3A%2222101%22%3Bs%3A12%3A%22neighborhood%22%3BN%3Bs%3A4%3A%22city%22%3Bs%3A6%3A%22Mclean%22%3Bs%3A6%3A%22county%22%3Bs%3A14%3A%22Fairfax+County%22%3Bs%3A5%3A%22state%22%3Bs%3A8%3A%22Virginia%22%3Bs%3A7%3A%22country%22%3Bs%3A13%3A%22United+States%22%3Bs%3A11%3A%22countrycode%22%3Bs%3A2%3A%22US%22%3Bs%3A9%3A%22statecode%22%3Bs%3A2%3A%22VA%22%3Bs%3A10%3A%22countycode%22%3BN%3Bs%3A8%3A%22timezone%22%3Bs%3A16%3A%22America%2FNew_York%22%3Bs%3A8%3A%22areacode%22%3Bs%3A3%3A%22571%22%3Bs%3A4%3A%22uzip%22%3Bs%3A5%3A%2222101%22%3Bs%3A4%3A%22hash%22%3BN%3Bs%3A5%3A%22woeid%22%3Bs%3A8%3A%2212766820%22%3Bs%3A7%3A%22woetype%22%3Bs%3A2%3A%2211%22%3B%7D; fsbotchecked=true; _pk_id.29.e1c2=22645f0de4fa62fc.1639342613.; _fssid=e247ef7b-3dba-4c48-9ef4-0b524c5c1029; _pbjs_userid_consent_data=3524755945110770; _pubcid=67b709a0-31f2-4083-9892-1c52ea90b24e; __qca=P0-1329109895-1639342614147; __gads=ID=515a5b651c15ac4a:T=1639342614:S=ALNI_MYLV5YsXYXY-bqgZBZTGGzMVRsr-w; download_form=1; _lr_env_src_ats=false; panoramaId_expiry=1639970132164; _cc_id=c152aba02997cc1975f5db00b4e405da; panoramaId=a7bb805649e71f2be388a7df8a724945a702e8757b95adef306fccd06981c5c0; cookie=%7B%22id%22%3A%2201FMZ3TFK7W9V0KD7D3DAGHYMH%22%2C%22ts%22%3A1639505137378%7D; _pk_ref.29.e1c2=%5B%22%22%2C%22%22%2C1639519693%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; cto_bidid=l2Lm319sN0N3NW5ZRHpjelZpcDFnNEJtbmJPbGxoTVhiNnUlMkZWNGY0dTFhM252JTJGenV5MmdHVWoxM1MlMkZrclZVQnRGcmZtZGV5TTdOSFgyRmEwa1dZUTlQdVhtYjBsTCUyQlJtUFZaOUhRTCUyQkN0WTMyQ3UxWlBkNVF3M2N1U2hUaHJyRUJtelA; cto_bundle=Q1-VMF9MS0tEU0lBaWxWNDJGOSUyQm8zcDNCQ244amlkdnpad0gxNHBBOWZFQ1hUSlp4ViUyRnpKV090T0xkNXEyMFd1UWY1YVlBQnp6a210YnAlMkZFSSUyRlBYaVRoa0NUV3VHUFdZQnc5R05iUHpIdVl2TnBETzhJd2pFWTg2enE1bzVtQTd2UyUyQlIlMkIxZ0xjdTFXcDRsejRxaVdNMk5hJTJCekM0NG1yZE1UN3pYR0Z5U1pnOWY5dyUzRA; cto_bundle=zFE5QF9MS0tEU0lBaWxWNDJGOSUyQm8zcDNCQ2dPanI2S2FKRjZiaCUyRk5pcGdwbmJUNjdSY0RkUk1oY2FmOXdwcUtIcmEyYk1wVUhwbEVaNThKWSUyRnYxTnA3JTJCOCUyRnVNMWVPWkRiZ0hLRDdvR01MNmMzJTJGMDlFT0JncGJFc1pBSVY5eUgzVUtiNEczQVd4b01SejR4UUpSY2RuR0xUVkx0Q1lrZnN4MmVjWWliJTJGeU5seHRoTSUzRA; cto_bundle=zFE5QF9MS0tEU0lBaWxWNDJGOSUyQm8zcDNCQ2dPanI2S2FKRjZiaCUyRk5pcGdwbmJUNjdSY0RkUk1oY2FmOXdwcUtIcmEyYk1wVUhwbEVaNThKWSUyRnYxTnA3JTJCOCUyRnVNMWVPWkRiZ0hLRDdvR01MNmMzJTJGMDlFT0JncGJFc1pBSVY5eUgzVUtiNEczQVd4b01SejR4UUpSY2RuR0xUVkx0Q1lrZnN4MmVjWWliJTJGeU5seHRoTSUzRA",
    "cookie": "__qca=P0-265110002-1716438146182; _pk_id.29.e1c2=850d2e5631f01cb3.1716438145.; _li_dcdm_c=.unitedstateszipcodes.org; _lc2_fpi=16307b161960--01hyhtz72w073g8865yva552gz; _lc2_fpi_meta=%7B%22w%22%3A1716438146140%7D; cookie=d5298dd1-0594-42f8-af68-55a72be7b2bf; cookie_cst=zix7LPQsHA%3D%3D; _lr_env_src_ats=false; pbjs_fabrickId=%7B%22fabrickId%22%3A%22E1%3ABBHbe7pp3jPpWXTyBwzBZIBD-XPVrbWLKeQaChrjyiMdiaUfIk6-eE5z2JP_xQme3zGhX0ZEVNVAf_RAh7MSONUJ4PBjkB8dF3j-Om48s3GslNc4Zn9IFsL00ikZlUch%22%7D; pbjs_fabrickId_cst=zix7LPQsHA%3D%3D; _au_1d=AU1D-0100-001716438146-Q7SJLMMZ-4NET; __qca=P0-265110002-1716438146182; _gid=GA1.2.1303140580.1716438147; ccuid=3cbd6276-780a-4208-91bf-b5eb273b3457; TAPAD=%7B%22id%22%3A%224ae7964a-4e14-450d-a5d2-fe2b589baf9e%22%7D; download_form=1; _lr_retry_request=true; _pk_ref.29.e1c2=%5B%22%22%2C%22%22%2C1716527156%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.29.e1c2=1; __gads=ID=1aa6584430d8abe3:T=1716438146:RT=1716527697:S=ALNI_MYGvYXRclGUCWQuCzc6zZOMMoVyWg; __gpi=UID=00000e2a5b1f8c71:T=1716438146:RT=1716527697:S=ALNI_MavHuyqiSkgJFtl7PR-P_zvrrBxbw; __eoi=ID=ecee0f5ad933ba92:T=1716438146:RT=1716527697:S=AA-AfjYKsO9LjqNRGJaMj0v0OBvt; cto_bundle=sC2Zh19vUEd6TkFCJTJGc2RxaXlJY2ZtVThoMWYwclAzc1klMkJPUVRQMDFtWXJTMFpPMSUyRlZJJTJCb3VFN3M0ZTF4aiUyQnpoMzJWN2xMVVdXYW5DQ3RNN2RhQTFVclBnNUp2NVpkWWZqclNLV2xranBXUWdRaXl3Y2NkSllOYjhPVU1kblE1SWRPZGxqeUdTUTl4aDRJbGhhT0hpZGNnNU1kVXZHdkoyV0Qzc0xab2t0QjFVVDQ3RDg5ckd5NDcxbEllYTg3U0lBZWhGd2tEUGVLVyUyQjlZanR2TXQyRyUyQnk2VnlwR0pzb1JBS0ZsZEZwR0VvV3FrVkFoNmlUN0FacGZGRXM4azVYMmZKUEg0bVBsYjVxTnQxUTlLZjlvZnNJeDMlMkZySzg1bDFobHdhVTJQTlNIS2VFR0xwZ3FEMndudzFGMWFQNkQ5JTJGTDQ2YzJhTGVaNlJoOG5id3hrRUFYbUcyaGclM0QlM0Q; cto_bidid=-LE-t18wVUJ0bXdYRldBZUY5RWFENSUyRnZ2TVlYcjg1SHN1JTJCOVg1S3IlMkJPc0UzS2Z6QWFJenNFZFhrR3BtRDFBMSUyQnhXVGI1VEZuU3FXSmNMYyUyQjR0UGFLa0Eyd2QlMkZES3l2RDlOZkkxOFd1dW1sJTJGUGd0dG5iaWptTGFjOERPcFZUdWJ1eGd1; _ga_FVWZ0RM4DH=GS1.1.1716527708.4.0.1716527712.56.0.0; _ga=GA1.1.1266298988.1716438147; datadome=dyfDhUhLiOHCO3wm9gW441xf4kLQ1MSmS~zLYjIQvXDETf6UHfaegLRaq2_ie8WaTCyyn_ovtOnVZrxM0RZTQUN0RBVSvpS~3lh7eJgOHXqDSJ94_hG6omyMVS86TcK4",
}


session = HTMLSession()
r = session.get("https://www.unitedstateszipcodes.org/20037/", headers=headers)
# r.html.render()
print("============")
# print(r.html)
print("_-----------------")
print(r.text)
# print("_-----------------")
# print(r.html.search("Stats and Demographics for the 20036 ZIP Code")[0])