import pprint

from helpers.icd.v11 import Chapter, Root, Category, Block


def test_root():
    data = {
        "@context": "http://id.who.int/icd/contexts/contextForTopLevel.json",
        "@id": "http://id.who.int/icd/release/11/2025-01/mms",
        "title": {
            "@language": "en",
            "@value": "ICD-11 for Mortality and Morbidity Statistics",
        },
        "releaseId": "2025-01",
        "availableLanguages": [
            "ar",
            "cs",
            "en",
            "es",
            "fr",
            "kk",
            "la",
            "pt",
            "ru",
            "sk",
            "sv",
            "tr",
            "uz",
            "zh",
        ],
        "releaseDate": "2025-01-24",
        "child": [
            "http://id.who.int/icd/release/11/2025-01/mms/1435254666",
            "http://id.who.int/icd/release/11/2025-01/mms/1630407678",
            "http://id.who.int/icd/release/11/2025-01/mms/1766440644",
            "http://id.who.int/icd/release/11/2025-01/mms/1954798891",
            "http://id.who.int/icd/release/11/2025-01/mms/21500692",
            "http://id.who.int/icd/release/11/2025-01/mms/334423054",
            "http://id.who.int/icd/release/11/2025-01/mms/274880002",
            "http://id.who.int/icd/release/11/2025-01/mms/1296093776",
            "http://id.who.int/icd/release/11/2025-01/mms/868865918",
            "http://id.who.int/icd/release/11/2025-01/mms/1218729044",
            "http://id.who.int/icd/release/11/2025-01/mms/426429380",
            "http://id.who.int/icd/release/11/2025-01/mms/197934298",
            "http://id.who.int/icd/release/11/2025-01/mms/1256772020",
            "http://id.who.int/icd/release/11/2025-01/mms/1639304259",
            "http://id.who.int/icd/release/11/2025-01/mms/1473673350",
            "http://id.who.int/icd/release/11/2025-01/mms/30659757",
            "http://id.who.int/icd/release/11/2025-01/mms/577470983",
            "http://id.who.int/icd/release/11/2025-01/mms/714000734",
            "http://id.who.int/icd/release/11/2025-01/mms/1306203631",
            "http://id.who.int/icd/release/11/2025-01/mms/223744320",
            "http://id.who.int/icd/release/11/2025-01/mms/1843895818",
            "http://id.who.int/icd/release/11/2025-01/mms/435227771",
            "http://id.who.int/icd/release/11/2025-01/mms/850137482",
            "http://id.who.int/icd/release/11/2025-01/mms/1249056269",
            "http://id.who.int/icd/release/11/2025-01/mms/1596590595",
            "http://id.who.int/icd/release/11/2025-01/mms/718687701",
            "http://id.who.int/icd/release/11/2025-01/mms/231358748",
            "http://id.who.int/icd/release/11/2025-01/mms/979408586",
        ],
        "browserUrl": "https://icd.who.int/browse/2025-01/mms/en",
    }
    result = Root.model_validate(data)
    pprint.pprint(result)


def test_child():
    data = {
        "@context": "http://id.who.int/icd/contexts/contextForLinearizationEntity.json",
        "@id": "http://id.who.int/icd/release/11/2025-01/mms/1435254666",
        "parent": ["http://id.who.int/icd/release/11/2025-01/mms"],
        "child": [
            "http://id.who.int/icd/release/11/2025-01/mms/588616678",
            "http://id.who.int/icd/release/11/2025-01/mms/1904876434",
            "http://id.who.int/icd/release/11/2025-01/mms/979278646",
            "http://id.who.int/icd/release/11/2025-01/mms/1539889147",
            "http://id.who.int/icd/release/11/2025-01/mms/1412960686",
            "http://id.who.int/icd/release/11/2025-01/mms/1935092859",
            "http://id.who.int/icd/release/11/2025-01/mms/487269828",
            "http://id.who.int/icd/release/11/2025-01/mms/1000704511",
            "http://id.who.int/icd/release/11/2025-01/mms/1104303944",
            "http://id.who.int/icd/release/11/2025-01/mms/1585949804",
            "http://id.who.int/icd/release/11/2025-01/mms/1959883044",
            "http://id.who.int/icd/release/11/2025-01/mms/921595235",
            "http://id.who.int/icd/release/11/2025-01/mms/1251496839",
            "http://id.who.int/icd/release/11/2025-01/mms/1136802325",
            "http://id.who.int/icd/release/11/2025-01/mms/145723401",
            "http://id.who.int/icd/release/11/2025-01/mms/985510409",
            "http://id.who.int/icd/release/11/2025-01/mms/1646490591",
            "http://id.who.int/icd/release/11/2025-01/mms/1939815950",
            "http://id.who.int/icd/release/11/2025-01/mms/255141529",
            "http://id.who.int/icd/release/11/2025-01/mms/293771399",
            "http://id.who.int/icd/release/11/2025-01/mms/1760597414",
            "http://id.who.int/icd/release/11/2025-01/mms/458687859",
            "http://id.who.int/icd/release/11/2025-01/mms/1435254666/unspecified",
        ],
        "browserUrl": "https://icd.who.int/browse/2025-01/mms/en#1435254666",
        "code": "01",
        "source": "http://id.who.int/icd/entity/1435254666",
        "classKind": "chapter",
        "foundationChildElsewhere": [
            {
                "label": {
                    "@language": "en",
                    "@value": "Infections of the fetus or newborn",
                },
                "foundationReference": "http://id.who.int/icd/entity/911707612",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/911707612",
            },
            {
                "label": {"@language": "en", "@value": "Human prion diseases"},
                "foundationReference": "http://id.who.int/icd/entity/1965146397",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/1965146397",
            },
            {
                "label": {"@language": "en", "@value": "Pneumonia"},
                "foundationReference": "http://id.who.int/icd/entity/142052508",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/142052508",
            },
        ],
        "title": {
            "@language": "en",
            "@value": "Certain infectious or parasitic diseases",
        },
        "definition": {
            "@language": "en",
            "@value": "This chapter includes certain conditions caused by pathogenic organisms or microorganisms, such as bacteria, viruses, parasites or fungi.",
        },
        "exclusion": [
            {
                "label": {
                    "@language": "en",
                    "@value": "Infection arising from device, implant or graft, not elsewhere classified",
                },
                "foundationReference": "http://id.who.int/icd/entity/1612485599",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/1612485599",
            }
        ],
        "relatedEntitiesInPerinatalChapter": ["http://id.who.int/icd/entity/911707612"],
    }
    result = Chapter.model_validate(data)
    pprint.pprint(result)


def test_category():
    data = {
        "@context": "http://id.who.int/icd/contexts/contextForLinearizationEntity.json",
        "@id": "http://id.who.int/icd/release/11/2025-01/mms/257068234",
        "parent": ["http://id.who.int/icd/release/11/2025-01/mms/135352227"],
        "browserUrl": "https://icd.who.int/browse/2025-01/mms/en#257068234",
        "code": "1A00",
        "source": "http://id.who.int/icd/entity/257068234",
        "classKind": "category",
        "postcoordinationScale": [
            {
                "@id": "http://id.who.int/icd/release/11/2025-01/mms/257068234/postcoordinationScale/infectiousAgent",
                "axisName": "http://id.who.int/icd/schema/infectiousAgent",
                "requiredPostcoordination": "false",
                "allowMultipleValues": "AllowAlways",
                "scaleEntity": [
                    "http://id.who.int/icd/release/11/2025-01/mms/194483911",
                    "http://id.who.int/icd/release/11/2025-01/mms/802386629",
                    "http://id.who.int/icd/release/11/2025-01/mms/21927667",
                ],
            },
            {
                "@id": "http://id.who.int/icd/release/11/2025-01/mms/257068234/postcoordinationScale/associatedWith",
                "axisName": "http://id.who.int/icd/schema/associatedWith",
                "requiredPostcoordination": "false",
                "allowMultipleValues": "AllowAlways",
                "scaleEntity": [
                    "http://id.who.int/icd/release/11/2025-01/mms/1215034670",
                    "http://id.who.int/icd/release/11/2025-01/mms/1839638766",
                    "http://id.who.int/icd/release/11/2025-01/mms/501791005",
                    "http://id.who.int/icd/release/11/2025-01/mms/1975056531",
                    "http://id.who.int/icd/release/11/2025-01/mms/828922344",
                    "http://id.who.int/icd/release/11/2025-01/mms/174465822",
                    "http://id.who.int/icd/release/11/2025-01/mms/612672352",
                    "http://id.who.int/icd/release/11/2025-01/mms/1882742628/other",
                    "http://id.who.int/icd/release/11/2025-01/mms/1882742628/unspecified",
                ],
            },
        ],
        "title": {"@language": "en", "@value": "Cholera"},
        "definition": {
            "@language": "en",
            "@value": "Cholera is a potentially epidemic and life-threatening infection of the intestine, characterised by extreme watery (secretory) diarrhoea often accompanied by vomiting, with rapid depletion of body fluids and salt that may result in hypovolemic shock and acidosis. Cholera outbreaks are caused by toxigenic strains of Vibrio cholerae serogroups O1 and O139. Serogroup O1 has two biovars; classical and eltor. Vibrio cholerae O1, biovar cholerae is classical type. Vibrio cholerae O1, biovar eltor is eltor type.",
        },
        "inclusion": [{"label": {"@language": "en", "@value": "cholera syndrome"}}],
        "fullySpecifiedName": {
            "@language": "en",
            "@value": "Intestinal infection due to Vibrio cholerae",
        },
        "relatedEntitiesInPerinatalChapter": ["http://id.who.int/icd/entity/911707612"],
        "indexTerm": [
            {"label": {"@language": "en", "@value": "Cholera"}},
            {"label": {"@language": "en", "@value": "cholera syndrome"}},
            {"label": {"@language": "en", "@value": "asiatic cholera"}},
            {"label": {"@language": "en", "@value": "epidemic cholera"}},
            {
                "label": {
                    "@language": "en",
                    "@value": "Intestinal infection due to Vibrio cholerae",
                }
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Enteritis due to cholera due to Vibrio cholerae, non-O1 strains",
                },
                "foundationReference": "http://id.who.int/icd/entity/1170831944",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Cholera due to Vibrio cholerae O1, biovar cholerae",
                },
                "foundationReference": "http://id.who.int/icd/entity/1205958647",
            },
            {
                "label": {"@language": "en", "@value": "classical cholera"},
                "foundationReference": "http://id.who.int/icd/entity/1205958647",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Enteritis due to Cholera due to Vibrio cholerae O1, biovar cholerae",
                },
                "foundationReference": "http://id.who.int/icd/entity/1384028266",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Enteritis due to classical cholera",
                },
                "foundationReference": "http://id.who.int/icd/entity/1384028266",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Cholera due to Vibrio cholerae O1, biovar eltor",
                },
                "foundationReference": "http://id.who.int/icd/entity/581614179",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "cholera - vibrio cholerae 01 eltor biotype",
                },
                "foundationReference": "http://id.who.int/icd/entity/581614179",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "cholera due to Vibrio cholerae 01, Cholera eltor",
                },
                "foundationReference": "http://id.who.int/icd/entity/581614179",
            },
            {
                "label": {"@language": "en", "@value": "cholera due to Cholera eltor"},
                "foundationReference": "http://id.who.int/icd/entity/581614179",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Enteritis due to cholera due to Vibrio cholerae O1, biovar eltor",
                },
                "foundationReference": "http://id.who.int/icd/entity/375406584",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Enteritis due to cholera due to Cholera eltor",
                },
                "foundationReference": "http://id.who.int/icd/entity/375406584",
            },
            {
                "label": {"@language": "en", "@value": "eltor enteritis"},
                "foundationReference": "http://id.who.int/icd/entity/375406584",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "infectious enteritis due to vibrio cholerae 01, biovar eltor",
                },
                "foundationReference": "http://id.who.int/icd/entity/375406584",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Cholera due to Vibrio cholerae O139",
                },
                "foundationReference": "http://id.who.int/icd/entity/1972085775",
            },
        ],
    }
    result = Category.model_validate(data)
    pprint.pprint(result)


def test_block():
    data = {
        "@context": "http://id.who.int/icd/contexts/contextForLinearizationEntity.json",
        "@id": "http://id.who.int/icd/release/11/2025-01/mms/911707612",
        "parent": ["http://id.who.int/icd/release/11/2025-01/mms/1306203631"],
        "child": [
            "http://id.who.int/icd/release/11/2025-01/mms/381388700",
            "http://id.who.int/icd/release/11/2025-01/mms/1935107489",
            "http://id.who.int/icd/release/11/2025-01/mms/1645664101",
            "http://id.who.int/icd/release/11/2025-01/mms/528118622",
            "http://id.who.int/icd/release/11/2025-01/mms/1945127438",
            "http://id.who.int/icd/release/11/2025-01/mms/188684108",
            "http://id.who.int/icd/release/11/2025-01/mms/911707612/other",
            "http://id.who.int/icd/release/11/2025-01/mms/911707612/unspecified",
        ],
        "browserUrl": "https://icd.who.int/browse/2025-01/mms/en#911707612",
        "code": "",
        "source": "http://id.who.int/icd/entity/911707612",
        "classKind": "block",
        "blockId": "BlockL1-KA6",
        "codeRange": "KA60-KA6Z",
        "foundationChildElsewhere": [
            {
                "label": {
                    "@language": "en",
                    "@value": "Fetus or newborn affected by maternal infectious diseases",
                },
                "foundationReference": "http://id.who.int/icd/entity/953221469",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/953221469",
            },
            {
                "label": {"@language": "en", "@value": "Congenital syphilis"},
                "foundationReference": "http://id.who.int/icd/entity/587996426",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/587996426",
            },
        ],
        "title": {"@language": "en", "@value": "Infections of the fetus or newborn"},
        "inclusion": [
            {
                "label": {
                    "@language": "en",
                    "@value": "infections acquired in utero or during birth",
                }
            }
        ],
        "exclusion": [
            {
                "label": {
                    "@language": "en",
                    "@value": "human immunodeficiency virus [HIV] disease",
                },
                "foundationReference": "http://id.who.int/icd/entity/1000704511",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/1000704511",
            },
            {
                "label": {"@language": "en", "@value": "Congenital pneumonia"},
                "foundationReference": "http://id.who.int/icd/entity/594985340",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/594985340",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "congenital gonococcal infection",
                },
                "foundationReference": "http://id.who.int/icd/entity/609214049",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/609214049",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Asymptomatic human immunodeficiency virus infection",
                },
                "foundationReference": "http://id.who.int/icd/entity/1511167574",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/574153866",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Gastroenteritis or colitis of infectious origin",
                },
                "foundationReference": "http://id.who.int/icd/entity/588616678",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/588616678",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Laboratory evidence of human immunodeficiency virus",
                },
                "foundationReference": "http://id.who.int/icd/entity/82994689",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/82994689",
            },
        ],
    }
    result = Block.model_validate(data)
    pprint.pprint(result)


def after_set(block, data):
    block = block.model_validate(data)


def test_after_model_validate():
    data = {
        "@context": "http://id.who.int/icd/contexts/contextForLinearizationEntity.json",
        "@id": "http://id.who.int/icd/release/11/2025-01/mms/911707612",
        "parent": ["http://id.who.int/icd/release/11/2025-01/mms/1306203631"],
        "child": [
            "http://id.who.int/icd/release/11/2025-01/mms/381388700",
            "http://id.who.int/icd/release/11/2025-01/mms/1935107489",
            "http://id.who.int/icd/release/11/2025-01/mms/1645664101",
            "http://id.who.int/icd/release/11/2025-01/mms/528118622",
            "http://id.who.int/icd/release/11/2025-01/mms/1945127438",
            "http://id.who.int/icd/release/11/2025-01/mms/188684108",
            "http://id.who.int/icd/release/11/2025-01/mms/911707612/other",
            "http://id.who.int/icd/release/11/2025-01/mms/911707612/unspecified",
        ],
        "browserUrl": "https://icd.who.int/browse/2025-01/mms/en#911707612",
        "code": "",
        "source": "http://id.who.int/icd/entity/911707612",
        "classKind": "block",
        "blockId": "BlockL1-KA6",
        "codeRange": "KA60-KA6Z",
        "foundationChildElsewhere": [
            {
                "label": {
                    "@language": "en",
                    "@value": "Fetus or newborn affected by maternal infectious diseases",
                },
                "foundationReference": "http://id.who.int/icd/entity/953221469",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/953221469",
            },
            {
                "label": {"@language": "en", "@value": "Congenital syphilis"},
                "foundationReference": "http://id.who.int/icd/entity/587996426",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/587996426",
            },
        ],
        "title": {"@language": "en", "@value": "Infections of the fetus or newborn"},
        "inclusion": [
            {
                "label": {
                    "@language": "en",
                    "@value": "infections acquired in utero or during birth",
                }
            }
        ],
        "exclusion": [
            {
                "label": {
                    "@language": "en",
                    "@value": "human immunodeficiency virus [HIV] disease",
                },
                "foundationReference": "http://id.who.int/icd/entity/1000704511",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/1000704511",
            },
            {
                "label": {"@language": "en", "@value": "Congenital pneumonia"},
                "foundationReference": "http://id.who.int/icd/entity/594985340",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/594985340",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "congenital gonococcal infection",
                },
                "foundationReference": "http://id.who.int/icd/entity/609214049",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/609214049",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Asymptomatic human immunodeficiency virus infection",
                },
                "foundationReference": "http://id.who.int/icd/entity/1511167574",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/574153866",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Gastroenteritis or colitis of infectious origin",
                },
                "foundationReference": "http://id.who.int/icd/entity/588616678",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/588616678",
            },
            {
                "label": {
                    "@language": "en",
                    "@value": "Laboratory evidence of human immunodeficiency virus",
                },
                "foundationReference": "http://id.who.int/icd/entity/82994689",
                "linearizationReference": "http://id.who.int/icd/release/11/2025-01/mms/82994689",
            },
        ],
    }
    block = Block(url="QAQ")
    after_set(block, data)
    pprint.pprint(block)
