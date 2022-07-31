import re


def find_para(text, key):
    # 通过关键字匹配找到domain的参数，返回列表
    if re.search('key', text):
        para_ch = re.findall(r'\d', text)
        eval('para = ' + para_ch)
    return para


def cal_nests_scope(i_parent_start, j_parent_start, e_we, e_sn, dx, dy,
                    ref_lat, ref_lon):
    # 计算各个nest的范围，返回经纬度
    d01





def main():
    re.purge()
    try:
        with open('namelist.wps', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                max_domain = find_para(line, max_domain)
                parent_id = find_para(line, parent_id)
                parent_grid_ratio = find_para(line, parent_grid_ratio)
                i_parent_start = find_para(line, i_parent_start)
                j_parent_start = find_para(line, j_parent_start)
                e_we = find_para(line, e_we)
                s_sn = find_para(line, s_sn)
                dx = find_para(line, dx)
                dy = find_para(line, dy)
                ref_lat = find_para(line, ref_lat)
                ref_lon = find_para(line, ref_lon)
                truelat1 = find_para(line, truelat1)
                truelat2 = find_para(line, truelat2)
                stand_lon = find_para(line, stand_lon)
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()
    
    
    
    open('domainInfo', 'w', encoding='utf-8') as f:
        f.write()

if __name__ == '__main__':
    main()