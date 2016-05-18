import tools
from chardet.universaldetector import UniversalDetector

def convert_dir(in_path):
    out_path=in_path+"_utf8"
    all_paths=[]
    path_cats,cats=tools.get_paths(in_path)
    for path_i,cat_i in zip(path_cats,cats):
        text_paths,names=tools.get_paths(path_i)
        all_paths+=text_paths
    tools.make_dir(out_path)
    for dir_i in path_cats:
        dir_i=dir_i.replace(in_path,out_path)
        tools.make_dir(dir_i)
    for in_path_i in all_paths:
        out_path_i=in_path_i.replace(in_path,out_path)
    	to_utf8(in_path_i,out_path_i)
    print(all_paths)

def to_utf8(in_path,out_path,encoding='ISO-8859-2'):
    text=tools.read(in_path)
    conv_text=text.decode(encoding).encode('utf-8')
    tools.save(out_path,conv_text)

def detect_encoding(path):
    u = UniversalDetector()
    for line in open(path, 'rb'):
        u.feed(line)
    u.close()
    result = u.result['encoding']
    print(result)
    return result	

convert_dir("lang")
#print(result)