import clusters
import tools
from metrics import lev

PATH=u'resources/lab4/'
LINES_FILE=PATH + u'lines.txt'
CLUSTER_FILE=PATH+ u'clusters.txt'

def create_clusters(in_file,out_file):
    clustered_lines=clusters.clustering(in_file)
    txt=clusters.save_cluster(clustered_lines)
    tools.save(out_file,txt)

def verify_clusters(in_file,out_file):
    in_cls=clusters.read_clusters(in_file)
    out_cls=clusters.read_clusters(out_file)
    in_cls=clusters.clusters_to_sets(in_file)
    out_cls=clusters.clusters_to_sets(in_file)
    return clusters.cluster_quality(in_cls,out_cls)

if __name__ == "__main__":
    verify_clusters(CLUSTER_FILE,PATH+u'my_clusters.txt')
    #create_clusters(LINES_FILE,PATH+u'my_clusters.txt')