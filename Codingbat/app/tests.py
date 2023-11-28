from django.test import SimpleTestCase

# Create your tests here.
class TestFontFont(SimpleTestCase):
    def test_font_times_Chocolate_2(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&num=2")
        self.assertContains(response, "ChoCho")
    
    def test_font_times_Chocolate_4(self):
        response = self.client.get("/warmup-2/font-times/?word=Chocolate&num=4")
        self.assertContains(response, "ChoChoChoCho")
    
    def test_font_times_abc_0(self):
        response = self.client.get("/warmup-2/font-times/?word=abc&num=0")
        self.assertContains(response, "")
    
    
    def test_no_teen_1_2_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=1&b=2&c=3")
        self.assertContains(response, 6)
    
    def test_no_teen_2_13_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=13&c=1")
        self.assertContains(response, 3)

    def test_no_teen_2_1_14(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=1&c=14")
        self.assertContains(response, 3)
    
    def test_xyz_there_abcxyz(self):
        response = self.client.get("/string-2/xyz-there/?xyz=abcxyz")
        self.assertContains(response, True)
    
    def test_xyz_there_abc_xyz(self):
        response = self.client.get("/string-2/xyz-there/?xyz=abc.xyz")
        self.assertContains(response, False)

    def test_xyz_there_xyz_abc(self):
        response = self.client.get("/string-2/xyz-there/?xyz=xyz.abc")
        self.assertContains(response, True)

    def test_avg_1_1_5_5_10_8_7(self):
        response = self.client.get("/list-2/centered-average/?num1=1&num2=1&num3=5&num4=5&num5=10&num6=8&num7=7")
        self.assertContains(response, 5)

    def test_avg_8_1_4_5_23_8_7(self):
        response = self.client.get("/list-2/centered-average/?num1=8&num2=1&num3=4&num4=5&num5=23&num6=8&num7=7")
        self.assertContains(response, 6)

    def test_avg_5_11_15_25_10_4_2(self):
        response = self.client.get("/list-2/centered-average/?num1=5&num2=11&num3=15&num4=25&num5=10&num6=4&num7=2")
        self.assertContains(response, 9)