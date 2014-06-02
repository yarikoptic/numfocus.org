SASS = sass

STATIC_DIR = static
SASS_DIR = $(STATIC_DIR)/scss
CSS_DIR = $(STATIC_DIR)/css

SASS_SOURCES = $(wildcard $(SASS_DIR)/*.scss)
SASS_CSS = $(patsubst $(SASS_DIR)/%.scss, $(CSS_DIR)/%.css, $(SASS_SOURCES))

all: $(SASS_CSS)

$(CSS_DIR)/%.css: $(SASS_DIR)/%.scss
	$(SASS) $< $@

clean:
	rm -rf $(SASS_CSS)

cleaner: clean
	rm -rf .sass-cache