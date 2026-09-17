# DB2ADMIN.WAREHOUSEITEMCOST

- **Module**: `WAREHOUSE` (high confidence — table name starts with 'WAREHOUSE')
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `COMPANYCODE`, `WAREHOUSEACCOUNTINGGROUPCODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `QUALITYLEVELCODE`, `STATISTICALGROUPCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 33091

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COSTIDENTIFIER` | DECIMAL(11,0) | NOT NULL |  |  |  |
| 3 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 15 | `STATISTICALGROUPCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 16 | `LASTINBOUNDCOST` | DECIMAL(18,5) |  |  |  |  |
| 17 | `LASTINBOUNDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 18 | `STANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 19 | `STANDARDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 20 | `WEIGHTEDAVERAGECOST` | DECIMAL(18,5) |  |  |  |  |
| 21 | `BASECOSTUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `DYNAMICAVERAGECOSTTOTALVALUE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `DYNAMICAVERAGECOSTTOTALQTY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `DYNAMICAVERAGECOSTUNITVALUE` | DECIMAL(18,5) |  |  |  |  |
| 25 | `HIFOCOST` | DECIMAL(18,5) |  |  |  |  |
| 26 | `HIFOCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 27 | `SECONDSTANDARDCOST` | DECIMAL(18,5) |  |  |  |  |
| 28 | `SNDSTANDARDCOSTLASTUPDATEDATE` | DATE |  |  |  |  |
| 29 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 30 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 31 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 32 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 33 | `WHSACCOUNTINGGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 34 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 35 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 36 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 38 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 39 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 40 | `LASTINBOUNDCOSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 41 | `WEIGHTEDAVERAGECOSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 42 | `DYNAMICAVERAGECOSTTOTVALSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 43 | `DYNAMICAVERAGECOSTUNITVLSNDCUR` | DECIMAL(18,5) |  |  |  |  |
| 44 | `HIFOCOSTSNDCUR` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WAREHOUSEITEMCOST.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WAREHOUSEITEMCOST.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND WAREHOUSEITEMCOST.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `UNITOFMEASURE_BASECOSTUNIT` | `BASECOSTUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `WAREHOUSEITEMCOST.BASECOSTUNITCODE = UNITOFMEASURE.CODE` |
| `WAREHOUSEACCOUNTINGGROUP_WAREHOUSEACCOUNTINGGROUP` | `WHSACCOUNTINGGROUPCOMPANYCODE`, `WAREHOUSEACCOUNTINGGROUPCODE` | [`WAREHOUSEACCOUNTINGGROUP`](../WAREHOUSE/WAREHOUSEACCOUNTINGGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `WAREHOUSEITEMCOST.WHSACCOUNTINGGROUPCOMPANYCODE = WAREHOUSEACCOUNTINGGROUP.COMPANYCODE AND WAREHOUSEITEMCOST.WAREHOUSEACCOUNTINGGROUPCODE = WAREHOUSEACCOUNTINGGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WAREHOUSEITEMCOSTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WAREHOUSEACCOUNTINGGROUPCODE,
       t.COSTIDENTIFIER,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.WAREHOUSEITEMCOST t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
