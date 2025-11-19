# ===========================================================
# blocks.py - St. Theresa Foundation Homepage Blocks
# Author: Jobet P. Casquejo
# ===========================================================

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

# -------------------------------
# 1. Hero Section Block
# -------------------------------
class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=100, help_text="Main heading for the hero section")
    subtitle = blocks.TextBlock(required=False, help_text="Optional subtitle")
    background_image = ImageChooserBlock(required=True, help_text="Background image for the hero section")
    call_to_action = blocks.URLBlock(required=False, help_text="Button URL for call to action")
    overlay_color = blocks.ChoiceBlock(
        choices=[
            ('var(--primary)', 'Primary'),
            ('var(--secondary)', 'Secondary'),
            ('var(--accent)', 'Accent')
        ],
        required=False,
        help_text="Optional overlay color (matches global CSS variables)"
    )

    class Meta:
        icon = "image"
        label = "Hero Section"
        template = "home/blocks/hero_block.html"


# -------------------------------
# 2. About Section Block
# -------------------------------
class AboutBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100, help_text="Heading for About section")
    content = blocks.RichTextBlock(required=True, help_text="Main content; supports rich text")
    image = ImageChooserBlock(required=False, help_text="Image for About section")
    reverse_layout = blocks.BooleanBlock(required=False, default=False, help_text="Check to reverse image/text layout on desktop")

    class Meta:
        icon = "doc-full"
        label = "About Section"
        template = "home/blocks/about_block.html"


# -------------------------------
# 3. Services / Programs Block
# -------------------------------
class ServiceStructBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=50)
    description = blocks.TextBlock(required=True, max_length=250)
    icon_name = blocks.CharBlock(required=False, max_length=50, help_text="Bulma or FontAwesome icon class")

class ServicesBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100)
    services_list = blocks.ListBlock(ServiceStructBlock(), help_text="Add multiple services or programs")

    class Meta:
        icon = "placeholder"
        label = "Services / Programs"
        template = "home/blocks/services_block.html"


# -------------------------------
# 4. Testimonials Block
# -------------------------------
class TestimonialStructBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True, max_length=50)
    role = blocks.CharBlock(required=False, max_length=50)
    content = blocks.TextBlock(required=True, max_length=300)
    avatar = ImageChooserBlock(required=False, help_text="Optional image/avatar of the person")

class TestimonialsBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100)
    testimonials = blocks.ListBlock(TestimonialStructBlock(), help_text="Add multiple testimonials")

    class Meta:
        icon = "user"
        label = "Testimonials"
        template = "home/blocks/testimonials_block.html"


# -------------------------------
# 5. Call-to-Action (CTA) Block
# -------------------------------
class CTAButtonStructBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(required=True, max_length=30, help_text="Text for CTA button")
    button_url = blocks.URLBlock(required=True, help_text="URL for CTA button")

class CTABlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100)
    subheading = blocks.TextBlock(required=False)
    buttons = blocks.ListBlock(CTAButtonStructBlock(), help_text="Add one or more buttons")
    background_color = blocks.ChoiceBlock(
        choices=[
            ('var(--primary)', 'Primary'),
            ('var(--secondary)', 'Secondary'),
            ('var(--accent)', 'Accent')
        ],
        required=False,
        help_text="Optional background color for CTA section"
    )

    class Meta:
        icon = "placeholder"
        label = "Call-to-Action"
        template = "home/blocks/cta_block.html"


# -------------------------------
# 6. Image Gallery Block
# -------------------------------
class GalleryBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100)
    images = blocks.ListBlock(ImageChooserBlock(), help_text="Add multiple images to gallery")
    gallery_layout = blocks.ChoiceBlock(
        choices=[('grid', 'Grid'), ('carousel', 'Carousel')],
        default='grid',
        help_text="Choose layout for the gallery"
    )

    class Meta:
        icon = "image"
        label = "Image Gallery"
        template = "home/blocks/gallery_block.html"


# -------------------------------
# 7. Newsletter Subscription Block
# -------------------------------
class NewsletterBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, max_length=100)
    subheading = blocks.TextBlock(required=False)
    form_action_url = blocks.URLBlock(required=True, help_text="AJAX submission URL for newsletter form")
    submit_button_text = blocks.CharBlock(required=True, default="Subscribe", max_length=20)

    class Meta:
        icon = "mail"
        label = "Newsletter Subscription"
        template = "home/blocks/newsletter_block.html"
