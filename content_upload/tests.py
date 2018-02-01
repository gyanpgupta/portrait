from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files import File
from django.utils.six import BytesIO

from .forms import UploadImageForm

from PIL import Image
from io import StringIO


def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
    """
    Generate a test image, returning the filename that it was saved as.

    If ``storage`` is ``None``, the BytesIO containing the image data
    will be passed instead.
    """
    data = BytesIO()
    Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename, image_file)


class UploadImageTests(TestCase):
    def setUp(self):
        super(UploadImageTests, self).setUp()


    def test_valid_form(self):
        '''
        valid post data should redirect
        The expected behavior is to show the image
        '''
        url = reverse('image')
        avatar = create_image(None, 'avatar.png')
        avatar_file = SimpleUploadedFile('front.png', avatar.getvalue())
        data = {'image': avatar_file}
        response = self.client.post(url, data, follow=True)
        image_src = response.context.get('image_src')

        self.assertEquals(response.status_code, 200)
        self.assertTrue(image_src)
        self.assertTemplateUsed('content_upload/result_image.html')


    def test_invalid_form(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('image')
        test_image = '/static/test.jpg'
        avatar_file = (StringIO("hi everyone"), 'test.txt')
        data = {'image': avatar_file}
        response = self.client.post(url, data, follow=True)
        form = response.context.get('form')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response,'Upload a valid image')
        self.assertTrue(form.errors)
        self.assertTemplateUsed('content_upload/upload_image.html')
       

    def test_invalid_post_data_empty_field(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('image')
        data = {'image': '',}
        response = self.client.post(url, data)
        form = response.context.get('form')

        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
        self.assertTemplateUsed('content_upload/upload_image.html')
        self.assertContains(response,'This field is required.')

