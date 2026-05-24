{% macro render_resource(r) -%}
- **[{{ r.name }}]({{ r.url }})** — {{ r.description }}
  {%- if r.people %} *People: {{ r.people | join(", ") }}.*{% endif %}
  {%- if r.location %} *({{ r.location }}{% if r.recurrence %}, {{ r.recurrence }}{% endif %})*{% endif %}
{{ "" }}
{% endmacro -%}

{% macro render_lab(r) -%}
- **[{{ r.name }}]({{ r.url }})**{% if r.institution %} [{{ r.institution }}]{% endif %} — {{ r.description }}
  {%- if r.people %} *People: {{ r.people | join(", ") }}.*{% endif %}
{{ "" }}
{% endmacro -%}

{% macro render_publication(r) -%}
- **[{{ r.name }}]({{ r.url }})** [{% if r.pub_format == 'blog' %}{% if r.people %}Personal {% endif %}Blog{% elif r.pub_format == 'newsletter' %}Newsletter{% else %}Substack{% endif %}] — {{ r.description }}
  {%- if r.people %} *People: {{ r.people | join(", ") }}.*{% endif %}
{{ "" }}
{% endmacro -%}
# MIR Guide — A community map for Music Information Retrieval

A community map of the people, labs, communities, and events shaping Music Information Retrieval.
Maintained as part of The Orchestral Pit, which runs a daily MIR research feed on Twitter/X ([@theOrchestralPit](https://x.com/theOrchestralPit)).

## What this is

MIR Guide maps the *who* and *where* of Music Information Retrieval — the labs doing the research, the communities where people gather, and the events where they meet. It is not a paper or library catalog; for those, see [yamathcy/awesome-music-informatics](https://github.com/yamathcy/awesome-music-informatics) and the [related lists](#related-lists) at the bottom of this page. The goal is a living reference for anyone trying to orient themselves in the MIR ecosystem.

## How to use this guide

Each entry carries a `source_type` — academic, industry, community, or media — that lets you filter by context. Browse the sections in order or jump directly to what you need. Filtering will become interactive on the companion site when it ships.

## Contents

- [Communities](#communities)
- [Events](#events)
  - [Conferences](#conferences)
  - [Festivals](#festivals)
  - [Meetups](#meetups)
- [Labs](#labs)
  - [Europe](#europe)
  - [North America](#north-america)
  - [Asia-Pacific](#asia-pacific)
  - [Industry](#industry)
- [Publications](#publications)
  - [Newsletters](#newsletters)
  - [Blogs](#blogs)
  - [Substacks](#substacks)
- [Podcasts](#podcasts)
- [Learning](#learning)
- [Related Lists](#related-lists)

---

## 👥 Communities

{% for r in communities %}
{{ render_resource(r) -}}
{% endfor %}

---

## 📅 Events

### 🎤 Conferences

{% for r in events_by_type.get('conference', []) %}
{{ render_resource(r) -}}
{% endfor %}

### 🎉 Festivals

{% for r in events_by_type.get('festival', []) %}
{{ render_resource(r) -}}
{% endfor %}

### ☕ Meetups

{% for r in events_by_type.get('meetup', []) %}
{{ render_resource(r) -}}
{% endfor %}

---

## 🔬 Labs

### 🇪🇺 Europe

{% for r in labs_by_region.get('europe', []) %}
{{ render_lab(r) -}}
{% endfor %}

### 🌎 North America

{% for r in labs_by_region.get('north-america', []) %}
{{ render_lab(r) -}}
{% endfor %}

### 🌏 Asia-Pacific

{% for r in labs_by_region.get('asia-pacific', []) %}
{{ render_lab(r) -}}
{% endfor %}

### 🏭 Industry

{% for r in labs_by_region.get('other', []) %}
{{ render_lab(r) -}}
{% endfor %}

---

## 📰 Publications

### 📧 Newsletters

{% for r in publications_by_format.get('newsletter', []) %}
{{ render_publication(r) -}}
{% endfor %}

### 📝 Blogs

{% for r in publications_by_format.get('blog', []) %}
{{ render_publication(r) -}}
{% endfor %}

### 📬 Substacks

{% for r in publications_by_format.get('substack', []) %}
{{ render_publication(r) -}}
{% endfor %}

---

## 🎙️ Podcasts

{% for r in podcasts %}
{{ render_resource(r) -}}
{% endfor %}

---

## 📚 Learning

{% for r in learning %}
{{ render_resource(r) -}}
{% endfor %}

---

## 🔗 Related Lists

{% for r in related_lists %}
{{ render_resource(r) -}}
{% endfor %}

---

## 🤝 Contributing

Found something missing or out of date? See [CONTRIBUTING.md](CONTRIBUTING.md) for how to suggest a resource via issue or open a pull request with a YAML edit.

## 📄 License

Code (scripts and workflows) is [MIT licensed](LICENSE). The curated content in `data/` is [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).

---

*Last built: {{ build_date }}*
