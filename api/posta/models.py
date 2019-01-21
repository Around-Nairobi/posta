from django.db import models

class errors(models.Model):
      message = models.CharField(max_length=100)
      type = models.CharField(max_length=100)
      code = models.IntegerField()
      fbtrace_id = models.IntegerField()

      def __str__(self):
          return self.message, self.type, self.code, self.fbtrace_id

