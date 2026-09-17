# DB2ADMIN.FINASSETSUBCODEIDENTIFICATION

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `BUSINESSUNITCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239494

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `SUBCODE01` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 5 | `SUBCODE02` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 6 | `SUBCODE03` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 7 | `SUBCODE04` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 8 | `SUBCODE05` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 9 | `SUBCODE06` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 10 | `SUBCODE07` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 11 | `SUBCODE08` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 12 | `SUBCODE09` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 13 | `SUBCODE10` | SMALLINT | NOT NULL |  | generic_classification_code |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINASSETSUBCODEIDENTIFICATION.COMPANYCODE = COMPANY.CODE` |
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINASSETSUBCODEIDENTIFICATION.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINASSETSUBCODEIDENTIFICATION.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ASSETSUBCODEIDENTIFICATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.FINASSETSUBCODEIDENTIFICATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
