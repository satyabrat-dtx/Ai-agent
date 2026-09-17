# DB2ADMIN.WRKSALESPRICEDEFINITION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 11665

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 5 | `INITIALDATE` | DATE |  |  |  |  |
| 6 | `FINALDATE` | DATE |  |  |  |  |
| 7 | `TEMPLATEDEFINITIONTYPE` | CHAR(1) |  |  |  |  |
| 8 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 9 | `PRICELISTCODE` | CHAR(8) |  |  |  |  |
| 10 | `PRICELISTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `COMPOUNDPRICEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `BREAKDOWNTYPE` | CHAR(2) |  |  |  |  |
| 13 | `UNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 14 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 15 | `PRICEUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 16 | `ORDERTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 17 | `AREACODE` | CHAR(3) |  |  |  |  |
| 18 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 19 | `COLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 20 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 21 | `AGENTCODE` | CHAR(3) |  |  |  |  |
| 22 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `FNCORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 24 | `ORDERCATEGORYCODE` | CHAR(3) |  |  |  |  |
| 25 | `ORDPRNGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 26 | `ORDERPARTNERGROUPCODE` | CHAR(3) |  |  |  |  |
| 27 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 28 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 29 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 34 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 35 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 36 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 37 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 38 | `ORDITEMGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 39 | `ORDERITEMGROUPCODE` | CHAR(3) |  |  |  |  |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 41 | `AREACOMPANYCODE` | CHAR(3) |  |  |  |  |
| 42 | `STATISTICALGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 43 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 44 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSALESPRICEDEFINITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.ORDERTYPE,
       t.INITIALDATE,
       t.FINALDATE,
       t.TEMPLATEDEFINITIONTYPE,
       t.TEMPLATECODE,
       t.PRICELISTCODE,
       t.PRICELISTTYPE,
       t.COMPOUNDPRICEREQUIRED
FROM   DB2ADMIN.WRKSALESPRICEDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
