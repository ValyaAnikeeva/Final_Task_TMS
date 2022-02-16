from tools.http_steps import add_pet, find_pet, update_name, find_name


def test_add_pet():
    """Этот тест добавляет нового питомца в магазин"""
    new_pet = {
        'id': 5,
        'name': 'zoro'
    }
    response = add_pet(new_pet)
    assert response.status_code == 200, 'wrong status code'
    assert '5' in response.text, 'no such pet id'


def test_find_pet():
    """Этот тест проверяет по Id добавлен ли питомец"""
    pet_id='5'
    response=find_pet(pet_id)
    assert response.status_code == 200, 'wrong status code'
    assert '5' in response.text, 'no such pet id'


def test_update_name():
    """С помощью этого теста обновляем данные питомцу (name)"""
    new_name = {
        'pet_id':'5',
        'name': 'morti'
    }
    response=update_name(new_name)
    assert response.status_code == 200, 'wrong status code'
    assert '5' in response.text, 'no such pet id'
    assert 'morti' in response.text, 'not found'


def test_find_name():
    """Этот тест проверяет по Id, что имя (name) обновлено"""
    pet_id='5'
    response=find_name(pet_id)
    assert response.status_code == 200, 'wrong status code'
    assert '5' in response.text, 'no such pet id'
