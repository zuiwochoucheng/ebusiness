K8S_VERSION=v1.13.3
ETCD_VERSION=3.2.18
DASHBOARD_VERSION=v1.8.3
FLANNEL_VERSION=v0.10.0-amd64
DNS_VERSION=1.1.3
PAUSE_VERSION=3.1
# 基本组件
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver-amd64:$K8S_VERSION
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager-amd64:$K8S_VERSION
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler-amd64:$K8S_VERSION
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy-amd64:$K8S_VERSION
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/etcd-amd64:$ETCD_VERSION
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/pause:$PAUSE_VERSION
docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:$DNS_VERSION
# 网络组件
docker pull quay.io/coreos/flannel:$FLANNEL_VERSION
# 修改tag
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-apiserver-amd64:$K8S_VERSION k8s.gcr.io/kube-apiserver-amd64:$K8S_VERSION
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-controller-manager-amd64:$K8S_VERSION k8s.gcr.io/kube-controller-manager-amd64:$K8S_VERSION
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-scheduler-amd64:$K8S_VERSION k8s.gcr.io/kube-scheduler-amd64:$K8S_VERSION
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-proxy-amd64:$K8S_VERSION k8s.gcr.io/kube-proxy-amd64:$K8S_VERSION
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/etcd-amd64:$ETCD_VERSION k8s.gcr.io/etcd-amd64:$ETCD_VERSION
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/pause:$PAUSE_VERSION k8s.gcr.io/pause:$PAUSE_VERSION
docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/coredns:$DNS_VERSION k8s.gcr.io/coredns:$DNS_VERSIONi
