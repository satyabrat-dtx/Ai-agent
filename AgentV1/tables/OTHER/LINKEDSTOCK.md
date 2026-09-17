# DB2ADMIN.LINKEDSTOCK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 61
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 1 constraint(s), references 8 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 214802

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `DESTINATIONORDER` | CHAR(2) | NOT NULL |  |  |  |
| 3 | `DESTINATIONABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 4 | `DLVSALORDLINESALORDCNTCODE` | CHAR(8) |  |  |  |  |
| 5 | `DLVSALORDERLINESALESORDERCODE` | CHAR(15) |  |  |  |  |
| 6 | `DLVSALESORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `DLVSALESORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `DLVSALORDLINECMPORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `RESERVATIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `RESERVATIONORDERCODE` | CHAR(15) |  |  |  |  |
| 12 | `RESERVATIONRESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 13 | `DELIVERYDATE` | DATE |  |  |  |  |
| 14 | `FINALLINK` | SMALLINT | NOT NULL |  |  |  |
| 15 | `REJECTEDLINK` | SMALLINT | NOT NULL |  |  |  |
| 16 | `SUBMITTEDJOBJOBNUMBER` | BIGINT | NOT NULL |  |  |  |
| 17 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `LOGICALWAREHOUSECODE` | CHAR(8) |  | FK | foreign_key |  |
| 21 | `DECOSUBCODE01` | CHAR(20) |  |  |  |  |
| 22 | `DECOSUBCODE02` | CHAR(10) |  |  |  |  |
| 23 | `DECOSUBCODE03` | CHAR(10) |  |  |  |  |
| 24 | `DECOSUBCODE04` | CHAR(10) |  |  |  |  |
| 25 | `DECOSUBCODE05` | CHAR(10) |  |  |  |  |
| 26 | `DECOSUBCODE06` | CHAR(10) |  |  |  |  |
| 27 | `DECOSUBCODE07` | CHAR(10) |  |  |  |  |
| 28 | `DECOSUBCODE08` | CHAR(10) |  |  |  |  |
| 29 | `DECOSUBCODE09` | CHAR(10) |  |  |  |  |
| 30 | `DECOSUBCODE10` | CHAR(10) |  |  |  |  |
| 31 | `QUALITYLEVELCODE` | DECIMAL(2,0) |  |  |  |  |
| 32 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 33 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 34 | `CONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 35 | `CONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 36 | `CONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 37 | `ELEMENTSSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 38 | `ELEMENTSCODE` | CHAR(15) |  |  |  |  |
| 39 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 40 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 41 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 42 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 43 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 44 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 45 | `STOCKTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 46 | `NEGATIVESTOCKTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 47 | `BALANCESTOCKTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 48 | `BASEPRIMARYUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 49 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 50 | `BASESECONDARYUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 51 | `BASESECONDARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 52 | `PACKAGINGCODE` | CHAR(3) |  |  |  |  |
| 53 | `PACKAGINGQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 54 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 55 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 56 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 57 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 58 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 59 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 60 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 8

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LINKEDSTOCK.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LINKEDSTOCK.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND LINKEDSTOCK.ITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGICALWAREHOUSE_LOGICALWAREHOUSE` | `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LINKEDSTOCK.LOGICALWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND LINKEDSTOCK.LOGICALWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `STOCKTYPE_BALANCESTOCKTYPE` | `BALANCESTOCKTYPECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `LINKEDSTOCK.BALANCESTOCKTYPECODE = STOCKTYPE.CODE` |
| `STOCKTYPE_NEGATIVESTOCKTYPE` | `NEGATIVESTOCKTYPECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `LINKEDSTOCK.NEGATIVESTOCKTYPECODE = STOCKTYPE.CODE` |
| `STOCKTYPE_STOCKTYPE` | `STOCKTYPECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `LINKEDSTOCK.STOCKTYPECODE = STOCKTYPE.CODE` |
| `UNITOFMEASURE_BASEPRIMARYUNIT` | `BASEPRIMARYUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `LINKEDSTOCK.BASEPRIMARYUNITCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_BASESECONDARYUNIT` | `BASESECONDARYUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `LINKEDSTOCK.BASESECONDARYUNITCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `LINKEDSTOCK_LINKEDSTOCK` | [`ALLOCATION`](../CORE_MASTER/ALLOCATION.md) | `COMPANYCODE`, `LINKEDSTOCKNUMBERID` | `ALLOCATION.COMPANYCODE = LINKEDSTOCK.COMPANYCODE AND ALLOCATION.LINKEDSTOCKNUMBERID = LINKEDSTOCK.NUMBERID` |

## Indexes

- `LINKEDSTOCKUID` (ABSUNIQUEID)
- `LINKEDSTOCK01` (DESTINATIONABSUNIQUEID, DESTINATIONORDER)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.DESTINATIONORDER,
       t.DESTINATIONABSUNIQUEID,
       t.DLVSALORDLINESALORDCNTCODE,
       t.DLVSALORDERLINESALESORDERCODE,
       t.DLVSALESORDERLINEORDERLINE,
       t.DLVSALESORDERLINEORDERSUBLINE,
       t.DLVSALORDLINECMPORDERLINE,
       t.DELIVERYDELIVERYLINE,
       t.RESERVATIONORDERCOUNTERCODE,
       t.RESERVATIONORDERCODE
FROM   DB2ADMIN.LINKEDSTOCK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
