import pygame

class EntityManager():
    def __init__(self, screen):
        self.screen = screen
        self.static_entities = []
        self.dynamic_entities = []
        self.static_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        self.static_dirty = True

    def add(self, entity, dynamic = True):
        if dynamic:
            self.dynamic_entities.append(entity)
        else:
            self.static_entities.append(entity)
            self.static_dirty = True

    def update(self):
        for entity in self.dynamic_entities:
            if entity.active:
                entity.update()

    def draw(self):
        # Redraw static surface if necessary
        if self.static_dirty:
            self.static_surface.fill((0, 0, 0, 0))  # Clear static surface
            for entity in self.static_entities:
                if entity.visible:
                    entity.draw(self.static_surface)
            self.static_dirty = False

        # Blit static layer
        self.screen.blit(self.static_surface, (0, 0))

        # Draw dynamic entities
        for entity in self.dynamic_entities:
            if entity.visible:
                entity.draw(self.screen)