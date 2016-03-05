
<body>
{% for obj in object_list %}
<a href='{{obj.get_absolute_url}}'><b> Title: </b>{{obj.title}}</a><br/>
<b> Content: </b>{{obj.content}}<br/>
<b> ID: </b>{{obj.id}}<br/>
<b> Created at: </b>{{obj.created}}<br/><br/><br/>
{% endfor %}