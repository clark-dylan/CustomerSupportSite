
$(window).on('load', function () {
    $searchEngine = $(".searchEngine");

    //Initialize the autocomplete object
    $searchEngine.autocomplete({minLength: 0});

    $searchEngine.keyup(function () {
        $searchTerm = $searchEngine.val();

        var query = {
            size: 6,
            query: {
                match_phrase_prefix: {
                    "title": {
                        query: $searchTerm
                    }
                }
            }
        };

        $.ajax({
            url: "http://localhost:9200/questions/_search",
            type: 'GET',
            dataType: 'JSON',
            contentType: 'application/json',
            data: {
                source: JSON.stringify(query),
                source_content_type: "application/json"
            },
            success: function (data) {
                showTerms(data);
            }
        });
    });
});
var showTerms = function (data) {
    $length = data["hits"]["hits"].length;
    $tag_arr = [];

    for ($i = 0; $i < $length; ++$i) {
        $tag_arr.push(data["hits"]["hits"][$i]["_source"]["title"]);
    }

    $(".searchEngine").autocomplete({
        source: $tag_arr
    });
};





