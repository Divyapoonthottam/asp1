import flask
import url_utilities
import domain_utilities

app=flask.Flask("my-python-server")

@app.route("/")
def title():
    return "<html><head><title>Divya's Project</title></head><body><h1>my server </body></html>"

@app.route("/find-meta-tag-with-name", methods=["GET"])
def find_meta_tag_with_name_for_url():
    request = flask.request
    request_args = request.args

    url = request_args["url"]
    meta_tag_name = request_args["meta-tag-name"]

    try:
        meta_tag_value = url_utilities.search_for_meta_tags_in_url(url, meta_tag_name)
    except Exception as ex:
        return flask.make_response(f"Bad request. Exception: {ex}", 400)

    if meta_tag_value is None:
        return flask.make_response(f"Meta tag with name '{meta_tag_name}' not found in '{url}'.", 404)
    else:
        api_response = {
            "meta-tag-value": meta_tag_value
        }
        return flask.make_response(api_response, 200)

@app.route("/check-txt-record", methods=["POST"])
def check_txt_record_for_url():
    request = flask.request
    request_json = request.json

    domain = request_json["domain"]
    txt_record = request_json["dns-txt-record"]

    try:
        txt_record_value = domain_utilities.search_for_txt_record_in_domain(domain, txt_record)
    except Exception as ex:
        return flask.make_response(f"Bad request. Exception: {ex}", 400)

    if txt_record_value is None:
        return flask.make_response(f"DNS TXT record '{txt_record}' not found for '{domain}'.", 404)
    else:
        api_response = {
            "dns-txt-record": txt_record
        }
        return flask.make_response(api_response, 200)

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 8080)