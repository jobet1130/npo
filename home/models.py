from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from .blocks import *

class HomePage(Page):
    subtitle = models.CharField(max_length=200, blank=True, help_text="Optional subtitle for the homepage")
    
    hero_block = StreamField([
        ('hero_section', HeroBlock()),
    ], use_json_field=True, blank=True)
    
    about_block = StreamField([
        ('about_section', AboutBlock()),
    ], use_json_field=True, blank=True)
    
    services_block = StreamField([
        ('services_section', ServicesBlock()),
    ], use_json_field=True, blank=True)
    
    testimonial_block = StreamField([
        ('testimonials_section', TestimonialsBlock()),
    ], use_json_field=True, blank=True)
    
    cta_block = StreamField([
        ('cta_section', CTABlock()),
    ], use_json_field=True, blank=True)
    
    gallery_block = StreamField([
        ('gallery_section', GalleryBlock()),
    ], use_json_field=True, blank=True)
    
    newsletter_block = StreamField([
        ('newsletter_section', NewsletterBlock()),
    ], use_json_field=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('hero_block'),
        FieldPanel('about_block'),
        FieldPanel('services_block'),
        FieldPanel('testimonial_block'),
        FieldPanel('cta_block'),
        FieldPanel('gallery_block'),
        FieldPanel('newsletter_block'),
    ]
    
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"