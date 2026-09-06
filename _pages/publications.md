---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<style>
    .pubs-list ol {
        margin-top: 0.7rem;
        padding-left: 1.4rem;
    }
    .pubs-list li {
        margin-bottom: 1rem;
    }
    .pub-title {
        font-weight: 700;
    }
    .pub-meta {
        color: #4f4f4f;
        margin: 0.2rem 0;
    }
    .pub-doi {
        margin: 0.1rem 0 0.6rem 0;
    }
</style>

My publications list is available on [Google Scholar](https://scholar.google.com/citations?user=ZC5pz7UAAAAJ&hl=en).

Selected publications from the CV (May 2024):

<section class="pubs-list">
    <h2>Selected Journal Publications</h2>
    <ol>
        <li>
            <div class="pub-title">Letter to the editor: on the paper "The double Pareto-Lognormal distribution - a new parametric model for size distributions" and its correction</div>
            <div class="pub-meta">Grbac, N.; Galinac Grbac, T. Communications in Statistics - Theory and Methods, 53(11), 4207-4209, 2024.</div>
            <div class="pub-doi"><a href="https://doi.org/10.1080/03610926.2023.2174788">DOI: 10.1080/03610926.2023.2174788</a></div>
        </li>
        <li>
            <div class="pub-title">The telehealth dilemma - Health-care deserts meet Internet's remote regions</div>
            <div class="pub-meta">Kathiravelu, P.; Fonovic, D.; Galinac Grbac, T.; et al. IEEE Computer, 56(9), 39-49, 2023.</div>
            <div class="pub-doi"><a href="https://doi.org/10.1109/MC.2023.3252945">DOI: 10.1109/MC.2023.3252945</a></div>
        </li>
        <li>
            <div class="pub-title">SCADA systems with focus on continuous manufacturing and steel industry: a survey on architectures, standards, challenges and industry 5.0</div>
            <div class="pub-meta">Sverko, M.; Galinac Grbac, T.; Mikuc, M. IEEE Access, 10, 109395-109430, 2022.</div>
            <div class="pub-doi"><a href="https://doi.org/10.1109/ACCESS.2022.3211288">DOI: 10.1109/ACCESS.2022.3211288</a></div>
        </li>
        <li>
            <div class="pub-title">Run-time interpretation of information system application models in mobile cloud environments</div>
            <div class="pub-meta">Tankovic, N.; Galinac Grbac, T. Computer Science and Information Systems, 17(1), 1-28, 2020.</div>
            <div class="pub-doi"><a href="https://doi.org/10.2298/CSIS180829021T">DOI: 10.2298/CSIS180829021T</a></div>
        </li>
        <li>
            <div class="pub-title">Software structure evolution and relation to subgraph defectiveness</div>
            <div class="pub-meta">Vrankovic, A.; Galinac Grbac, T.; Car, Z. IET Software, 13(5), 355-367, 2019.</div>
            <div class="pub-doi"><a href="https://doi.org/10.1049/iet-sen.2018.5060">DOI: 10.1049/iet-sen.2018.5060</a></div>
        </li>
    </ol>

    <h2>Selected Conference and Book-Chapter Publications</h2>
    <ol>
        <li>
            <div class="pub-title">The role of functional programming in management and orchestration of virtualized network resources. Part II</div>
            <div class="pub-meta">Galinac Grbac, T.; Domazet, N. LNCS 11950, 2023.</div>
            <div class="pub-doi"><a href="https://doi.org/10.1007/978-3-031-42833-3_5">DOI: 10.1007/978-3-031-42833-3_5</a></div>
        </li>
        <li>
            <div class="pub-title">Integrating SDN and NFV with QoS-aware service composition</div>
            <div class="pub-meta">Cardellini, V.; Galinac Grbac, T.; Kassler, A.; et al. In Autonomous Control for a Reliable Internet of Services, 2018.</div>
            <div class="pub-doi"><a href="https://doi.org/10.1007/978-3-319-90415-3_9">DOI: 10.1007/978-3-319-90415-3_9</a></div>
        </li>
        <li>
            <div class="pub-title">Performance optimization in transition toward open industrial control systems</div>
            <div class="pub-meta">Sverko, M.; Galinac Grbac, T.; Huljenic, D. SoftCOM 2023.</div>
            <div class="pub-doi"><a href="https://doi.org/10.23919/SoftCOM58365.2023.10271622">DOI: 10.23919/SoftCOM58365.2023.10271622</a></div>
        </li>
        <li>
            <div class="pub-title">Algorithms for sustainable system topologies</div>
            <div class="pub-meta">Galinac Grbac, T.; Grbac, N. 2022.</div>
            <div class="pub-doi"><a href="https://doi.org/10.48550/arxiv.2204.13993">DOI: 10.48550/arxiv.2204.13993</a></div>
        </li>
        <li>
            <div class="pub-title">Complex systems - network component security of SCADA systems</div>
            <div class="pub-meta">Sverko, M.; Galinac Grbac, T. MIPRO 2021.</div>
            <div class="pub-doi"><a href="https://doi.org/10.23919/MIPRO52101.2021.9596701">DOI: 10.23919/MIPRO52101.2021.9596701</a></div>
        </li>
    </ol>
</section>


{% include base_path %}

{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
{% endfor %}
