# :cloud:Surrounded by the Clouds: a Comprehensive Cloud Reachability Study:cloud::cloud:

Lorenzo Corneo<sup>1</sup>, Maximilian Eder<sup>2</sup>, Nitinder
Mohan<sup>2</sup>, Aleksandr Zavodovski<sup>1</sup>, Suzan
Bayhan<sup>3</sup>, Walter Wong<sup>4</sup>, Per Gunningberg<sup>1</sup>,
Jussi Kangasharju<sup>4</sup>,Jörg Ott<sup>2</sup>

Uppsala University<sup>1</sup>, Technical University of
Munich<sup>2</sup>, University of Twente<sup>3</sup>, University of
Helsinki<sup>4</sup>


---


This repository contains useful code to replicate the results that are
included in our publication *Surrounded by the Clouds: A Comprehensive
Cloud Reachability Study*, which is accepted at **The Web Conference
2021**:tada::sparkler:. Check the paper out
[here](https://lorenzocorneo.github.io/papers/2021-www.pdf):page_with_curl::page_with_curl:


---


# Abstract

In the early days of cloud computing, datacenters were sparsely
deployed at distant locations far from end-users with high end-to-end
communication latency. However, today's cloud datacenters have become
more geographically spread, the bandwidth of the networks keeps
increasing, pushing the end-users latency down.  In this paper, we
provide a comprehensive cloud reachability study as we perform
extensive global client-to-cloud latency measurements towards 189
datacenters from all major cloud providers. We leverage the well-known
measurement platform RIPE Atlas, involving up to 8500 probes deployed
in heterogeneous environments, e.g., home and offices. Our goal is to
evaluate the suitability of modern cloud environments for various
current and predicted applications. We achieve this by comparing our
latency measurements against known human perception thresholds and are
able to draw inferences on the suitability of current clouds for novel
applications, such as augmented reality. Our results indicate that the
current cloud coverage can easily support several latency-critical
applications, like cloud gaming, for the majority of the world’s
population.


---


# Dataset

The raw dataset is available at
[mediaTUM](https://mediatum.ub.tum.de/1593899) with detailed
information on how to set it up. We encourage to cite this dataset in
academic publications upon usage.

```
@misc{dataset,
	author = {Eder, Maximilian and Corneo, Lorenzo and Mohan, Nitinder and Zavodovski, Aleksandr and Bayhan, Suzan and Wong, Walter and Gunningberg, Per and Kangasharju, Jussi and Ott, Jörg},
	title = {Surrounded by the Clouds},
	publisher = {Technical University of Munich},
	url = {https://mediatum.ub.tum.de/1593899},
    doi = {10.14459/2020mp1593899},
    year = 2021,
	type = {Dataset},
	keywords = {Cloud, Edge computing; RIPE Atlas; Cloud connectivity; Internet measurements},
	abstract = {Cloud datacenter to user connectivity dataset collected over RIPE Atlas. The dataset accompanies research article "Surrounded by the Cloud" accepted at The Web Conference 2021},
	language = {en},
}
```

The data consists of a 60GB SQLite3 database that contains all the
measurements taken with the RIPE Atlas platform. The dataset includes
both `ping`s, `traceroute`s and information regarding the ownership of
the identified IP addresses.


---


# Usage instructions :construction_worker:

In order to reproduce our results, some non-default Python libraries
need to be installed with the following command:

```
pip install -r requirements.txt
```

In order to make the results replication smoother, we provide
pre-fetched data and avoid extremely time-consuming queries to the
SQLite3 database. However, these pre-fetcehd data were extracted by
the very same databese. In order to access such data, unzip
`data/data.zip` and delete the compressed file (if you wish). Then,
run the following command, from the folder's root, to generate all the
figures from the paper.

```sh generate_figure.sh```

The output of the script will be placed in the `figures/` folder and
each figure will be named after the figure identifier from the paper.


---


# Contact

Please feel free to contact me for further details at
<lorenzo.corneo@it.uu.se>.
