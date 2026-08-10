from typing import Any


class Column:
    @staticmethod
    def has_code(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "code" in raw_data.keys():
            cooked_data["code"] = raw_data["code"]

    @staticmethod
    def has_title(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "title" in raw_data.keys():
            cooked_data["title"] = raw_data["title"]["@value"]

    @staticmethod
    def has_fully_specified_name(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "fullySpecifiedName" in raw_data.keys():
            cooked_data["fully_specified_name"] = raw_data["fullySpecifiedName"]["@value"]

    @staticmethod
    def has_description(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "definition" in raw_data.keys():
            cooked_data["description"] = raw_data["definition"]["@value"]

    @staticmethod
    def has_inclusion(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "inclusion" in raw_data.keys():
            cooked_data["inclusion"] = [item["label"]["@value"] for item in raw_data["inclusion"]]

    @staticmethod
    def has_exclusions(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "exclusion" in raw_data.keys():
            cooked_data["exclusions"] = [item["label"]["@value"] for item in raw_data["exclusion"]]

    @staticmethod
    def has_all_index_terms(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "indexTerm" in raw_data.keys():
            cooked_data["all_index_terms"] = [item["label"]["@value"] for item in raw_data["indexTerm"]]

    @staticmethod
    def has_coded_elsewhere(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "foundationChildElsewhere" in raw_data.keys():
            cooked_data["coded_elsewhere"] = [
                {
                    "title": item["label"]["@value"],
                    "reference_url": item["linearizationReference"],
                }
                for item in raw_data["foundationChildElsewhere"]
            ]

    @staticmethod
    def has_browser_url(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "browserUrl" in raw_data.keys():
            cooked_data["browser_url"] = raw_data["browserUrl"]

    @staticmethod
    def has_class_kind(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "classKind" in raw_data.keys():
            cooked_data["class_kind"] = raw_data["classKind"]

    @staticmethod
    def has_child(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "child" in raw_data.keys():
            cooked_data["child"] = [{"url": item} for item in raw_data["child"]]

    @staticmethod
    def has_id_url(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "@id" in raw_data.keys():
            cooked_data["url"] = raw_data["@id"]

    @staticmethod
    def has_related_entities_in_perinatal_chapter(raw_data: dict[str, Any], cooked_data: dict[str, Any]):
        if "relatedEntitiesInPerinatalChapter" in raw_data.keys():
            cooked_data["related_entities_in_perinatal_chapter"] = raw_data["relatedEntitiesInPerinatalChapter"]
