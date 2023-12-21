from fastapi.testclient import TestClient
from api import app


def test_tokenizer_endpoint():

    # Arrange
    client = TestClient(app)
    text_to_tokenizer = 'Съешь [же] ещё этих мягких французских булок да выпей чаю.'

    # Act
    response = client.post("/tokenizer", json={"text": text_to_tokenizer})

    # Assert
    assert response.status_code == 200
    assert "response" in response.json()
    assert {
        "response": "{\"text\":{\"0\":\"Съешь\",\"1\":\"[\",\"2\":\"же\",\"3\":\"]\",\"4\":\"ещё\",\"5\":\"этих\","
                    "\"6\":\"мягких\",\"7\":\"французских\",\"8\":\"булок\",\"9\":\"да\",\"10\":\"выпей\",\"11\":\"чаю\","
                    "\"12\":\".\"},\"pos\":{\"0\":\"VERB\",\"1\":\"PUNCT\",\"2\":\"PART\",\"3\":\"PUNCT\",\"4\":\"ADV\","
                    "\"5\":\"DET\",\"6\":\"ADJ\",\"7\":\"ADJ\",\"8\":\"NOUN\",\"9\":\"CCONJ\",\"10\":\"NOUN\",\"11\":\"VERB\","
                    "\"12\":\"PUNCT\"},\"dep\":{\"0\":\"ROOT\",\"1\":\"punct\",\"2\":\"advmod\",\"3\":\"punct\",\"4\":\"advmod\","
                    "\"5\":\"det\",\"6\":\"amod\",\"7\":\"amod\",\"8\":\"obj\",\"9\":\"cc\",\"10\":\"nmod\",\"11\":\"obj\",\"12\":\"punct\"}}"
    } == response.json()


if __name__ == '__mian__':
    test_tokenizer_endpoint()
