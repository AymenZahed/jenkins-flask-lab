from app import app


def test_home():
    response = app.test_client().get('/')
    assert response.status == 200
    assert b"Jenkins CI/CD Lab" in response.data
    
    
def test_health():
    response = app.test_client().get("/health")
    
    
    assert response.status == 200
    assert response.get_json() == {"status" : "ok"}

