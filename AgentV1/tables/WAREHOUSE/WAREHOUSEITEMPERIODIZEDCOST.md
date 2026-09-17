# DB2ADMIN.WAREHOUSEITEMPERIODIZEDCOST

- **Module**: `WAREHOUSE` (high confidence — table name starts with 'WAREHOUSE')
- **Roles**: `business_data`
- **Columns**: 48
- **Primary key**: `COMPANYCODE`, `WAREHOUSEACCOUNTINGGROUPCODE`, `PERPERIODIZEDCALENDARTYPECODE`, `PERIODPERIODIZEDCALENDARYEAR`, `PERIODCODE`, `ITEMTYPEAFICODE`, `QUALITYLEVELCODE`, `STATISTICALGROUPCODE`, `COSTIDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 33179

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PERPERIODIZEDCALENDARTYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PERIODPERIODIZEDCALENDARYEAR` | DECIMAL(4,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PERIODCODE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `COSTIDENTIFIER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 6 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 8 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 18 | `STATISTICALGROUPCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 19 | `LASTINBOUNDCOST` | DECIMAL(18,5) |  |  |  |  |
| 20 | `LASTINBOUNDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 21 | `STANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 22 | `STANDARDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 23 | `WEIGHTEDAVERAGECOST` | DECIMAL(18,5) |  |  |  |  |
| 24 | `BASECOSTUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 25 | `DYNAMICAVERAGECOSTTOTALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 26 | `DYNAMICAVERAGECOSTTOTALQTY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `DYNAMICAVERAGECOSTUNITVALUE` | DECIMAL(18,5) |  |  |  |  |
| 28 | `HIFOCOST` | DECIMAL(18,5) |  |  |  |  |
| 29 | `HIFOCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 30 | `SECONDSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 31 | `SNDSTANDARDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 32 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 33 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 34 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 35 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 36 | `WHSACCOUNTINGGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 37 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 38 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 39 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 41 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 42 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 43 | `LASTINBOUNDCOSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 44 | `WEIGHTEDAVERAGECOSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 45 | `DYNAMICAVERAGECOSTTOTVALSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 46 | `DYNAMICAVERAGECOSTUNITVLSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 47 | `HIFOCOSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WAREHOUSEITEMPERIODIZEDCOST.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WAREHOUSEITEMPERIODIZEDCOST.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND WAREHOUSEITEMPERIODIZEDCOST.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `PERIOD_PERIOD` | `PERPERIODIZEDCALENDARTYPECODE`, `PERIODPERIODIZEDCALENDARYEAR`, `PERIODCODE` | [`PERIOD`](../WAREHOUSE/PERIOD.md) | `PERIODIZEDCALENDARTYPECODE`, `PERIODIZEDCALENDARYEAR`, `CODE` | RESTRICT | `WAREHOUSEITEMPERIODIZEDCOST.PERPERIODIZEDCALENDARTYPECODE = PERIOD.PERIODIZEDCALENDARTYPECODE AND WAREHOUSEITEMPERIODIZEDCOST.PERIODPERIODIZEDCALENDARYEAR = PERIOD.PERIODIZEDCALENDARYEAR AND WAREHOUSEITEMPERIODIZEDCOST.PERIODCODE = PERIOD.CODE` |
| `UNITOFMEASURE_BASECOSTUNIT` | `BASECOSTUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `WAREHOUSEITEMPERIODIZEDCOST.BASECOSTUNITCODE = UNITOFMEASURE.CODE` |
| `WAREHOUSEACCOUNTINGGROUP_WAREHOUSEACCOUNTINGGROUP` | `WHSACCOUNTINGGROUPCOMPANYCODE`, `WAREHOUSEACCOUNTINGGROUPCODE` | [`WAREHOUSEACCOUNTINGGROUP`](../WAREHOUSE/WAREHOUSEACCOUNTINGGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WAREHOUSEITEMPERIODIZEDCOST.WHSACCOUNTINGGROUPCOMPANYCODE = WAREHOUSEACCOUNTINGGROUP.COMPANYCODE AND WAREHOUSEITEMPERIODIZEDCOST.WAREHOUSEACCOUNTINGGROUPCODE = WAREHOUSEACCOUNTINGGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WHSITEMPERIODCOST1` (COSTIDENTIFIER, PERIODPERIODIZEDCALENDARYEAR, ITEMTYPEAFICODE, STATISTICALGROUPCODE, PERIODCODE, QUALITYLEVELCODE, PERPERIODIZEDCALENDARTYPECODE, WAREHOUSEACCOUNTINGGROUPCODE, COMPANYCODE)
- `WHSITEMPERIODCOST2` (ITEMTYPEAFICODE, COSTIDENTIFIER, PERIODPERIODIZEDCALENDARYEAR, STATISTICALGROUPCODE, PERIODCODE, QUALITYLEVELCODE, PERPERIODIZEDCALENDARTYPECODE, WAREHOUSEACCOUNTINGGROUPCODE, COMPANYCODE)
- `WHSITEMPERIODIZEDCOSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WAREHOUSEACCOUNTINGGROUPCODE,
       t.PERPERIODIZEDCALENDARTYPECODE,
       t.PERIODPERIODIZEDCALENDARYEAR,
       t.PERIODCODE,
       t.COSTIDENTIFIER,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05
FROM   DB2ADMIN.WAREHOUSEITEMPERIODIZEDCOST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
