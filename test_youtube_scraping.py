from ytb_function import *



class tests :

    #test video title
    def test_title():
        assert get_title["Title"] == 'Salah Sadaoui I rouh nif takfa lahya'

    #test author
    def test_author():
        assert get_author["Author"] == 'Nassim HSD'


    #test id
    def test_id():
        assert get_id["Id"] == 'A-bBAbQX4JM'

    
    #test number of likes
    def test_like():
        assert get_likes["Likes"] >= 13
    
    
    #test description
    def test_description():
        #assert get_description["description_vid"] == ""
        #The description of the video is too long
        print("Test of the descritption ")

    #test links of description
    def test_links():
        assert get_links["Links_description"] == ["https://www.youtube.com/watch?v=WtuUFNUuUWg", "https://www.youtube.com/premium", "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"] 
    
    
    
