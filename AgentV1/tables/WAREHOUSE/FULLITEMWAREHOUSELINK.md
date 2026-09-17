# DB2ADMIN.FULLITEMWAREHOUSELINK

- **Module**: `WAREHOUSE` (low confidence — FK neighbourhood: 1 of 1 related tables are WAREHOUSE)
- **Roles**: `business_data`
- **Columns**: 39
- **Primary key**: `COMPANYCODE`, `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 21502

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 14 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 16 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 17 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 18 | `ABCCODE` | CHAR(2) |  |  |  |  |
| 19 | `STOCKTAKEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 20 | `STOCKTAKESTANDARDGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 21 | `STOCKTAKECODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `TRNNUMBERFROMLASTSTOCKTAKE` | INTEGER | NOT NULL |  |  |  |
| 23 | `INVENTORYTURNOVERFACTOR` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 24 | `REORDERPOINT` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 25 | `SAFETYSTOCK` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 26 | `LASTTRANSACTIONDATE` | DATE |  |  |  |  |
| 27 | `LASTENTRYDATE` | DATE |  |  |  |  |
| 28 | `CURRENTSTOCKTAKEDATE` | DATE |  |  |  |  |
| 29 | `LASTSTOCKTAKEDATE` | DATE |  |  |  |  |
| 30 | `UNDERSTOCKTAKE` | CHAR(2) |  |  |  |  |
| 31 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 32 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 33 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 34 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 36 | `STOCKTAKESTDGRPTYPECMYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 37 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 38 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FULLITEMWAREHOUSELINK.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FULLITEMWAREHOUSELINK.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND FULLITEMWAREHOUSELINK.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `LOGICALWAREHOUSE_LOGICALWAREHOUSE` | `LOGICALWAREHOUSECOMPANYCODE`, `LOGICALWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FULLITEMWAREHOUSELINK.LOGICALWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND FULLITEMWAREHOUSELINK.LOGICALWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `STANDARDGROUP_STOCKTAKE` | `STOCKTAKESTDGRPTYPECMYCODE`, `STOCKTAKESTANDARDGROUPTYPECODE`, `STOCKTAKECODE` | [`STANDARDGROUP`](../CORE_MASTER/STANDARDGROUP.md) | `STANDARDGROUPTYPECOMPANYCODE`, `STANDARDGROUPTYPECODE`, `CODE` | RESTRICT | `FULLITEMWAREHOUSELINK.STOCKTAKESTDGRPTYPECMYCODE = STANDARDGROUP.STANDARDGROUPTYPECOMPANYCODE AND FULLITEMWAREHOUSELINK.STOCKTAKESTANDARDGROUPTYPECODE = STANDARDGROUP.STANDARDGROUPTYPECODE AND FULLITEMWAREHOUSELINK.STOCKTAKECODE = STANDARDGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FULLITEMWAREHOUSELINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.FULLITEMWAREHOUSELINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
