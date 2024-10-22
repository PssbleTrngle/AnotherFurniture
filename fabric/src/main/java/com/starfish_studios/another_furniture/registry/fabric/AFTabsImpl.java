package com.starfish_studios.another_furniture.registry.fabric;

import com.starfish_studios.another_furniture.AnotherFurniture;
import com.starfish_studios.another_furniture.registry.AFBlocks;
import com.starfish_studios.another_furniture.registry.AFRegistry;
import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.core.Registry;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;

public class AFTabsImpl {
    public static final CreativeModeTab AFM_TAB = Registry.register(BuiltInRegistries.CREATIVE_MODE_TAB,
            AnotherFurniture.res("tab"),
            FabricItemGroup.builder().title(Component.translatable("item_group." + AnotherFurniture.MOD_ID + ".tab"))
            .icon(() -> new ItemStack(AFBlocks.OAK_CHAIR.get().asItem())).displayItems((parameters, output) -> {
                output.acceptAll(AFRegistry.getAllModItems());
            }).build());

    public static void register() {}
}
