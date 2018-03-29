# coding=utf-8
import os


# 打开日志文件所在路径，按时间倒叙排列目录中的日志文件
def read_log_dir(log_dir, last_filename):
    log_filenames = []

    filenames = os.listdir(log_dir)  # 列出目录的下所有文件保存到lists
    filenames.sort(key=lambda fn: os.path.getmtime(os.path.join(log_dir, fn)), reverse=True)  # 按文件修改时间倒叙排列
    for filename in filenames:
        if filename == last_filename:
            break
        log_filenames.append(filename)

    return log_filenames


# 读取日志文件，返回一个字典
def read_log_file(log_file):
    result = []
    with open(log_file, 'r') as f:
        for line in f.readlines():
            words = line.split()
            if len(words) != 29:
                continue

            result.append(
                dict(
                    record_id=words[0],
                    event_timestamp=words[1],
                    acct_status_type=words[2],
                    called_station_id=words[3],
                    calling_station_id=words[4],
                    cisco_avpair_ssid=words[5],
                    cisco_avpair_nas_location=words[6],
                    cisco_avpair_vlan_id=words[7],
                    cisco_avpair_auth_algo_type=words[8],
                    cisco_avpair_connect_progress=words[9],
                    acct_authentic=words[10],
                    acct_session_time=words[11],
                    user_name=words[12],
                    acct_session_id=words[13],
                    acct_output_octets=words[14],
                    acct_input_octets=words[15],
                    acct_output_packets=words[16],
                    acct_input_packets=words[17],
                    acct_terminate_cause=words[18],
                    request_cisco_avpair_disc_cause_ext=words[19],
                    nas_port_type=words[20],
                    cisco_nas_port=words[21],
                    nas_port=words[22],
                    nas_ip_address=words[23],
                    service_type=words[24],
                    acct_delay_time=words[25],
                    proxy_type=words[26],
                    gpp2_correlation_id=words[27],
                    acct_unique_session_id=words[28],
                )
            )

    return result


if __name__ == '__main__':
    content = read_log_file('2018030712307908')
    print content
    print len(content)
