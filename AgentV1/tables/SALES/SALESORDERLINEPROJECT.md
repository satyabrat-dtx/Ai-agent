# DB2ADMIN.SALESORDERLINEPROJECT

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `SOLINESALESORDERCOUNTERCODE`, `SOLINESALESORDERCODE`, `SOLINEORDERLINE`, `SOLINEORDERSUBLINE`, `SOLINECOMPONENTORDERLINE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194094

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LINENO` | BIGINT | NOT NULL |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `SOLINESALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SOLINESALESORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SOLINEORDERLINE` | DECIMAL(5,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SOLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `SOLINECOMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `PROJECTCODE` | CHAR(20) |  | FK | foreign_key |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `ITEMCLOSERREMARKS` | VARCHAR(200) |  |  |  |  |
| 20 | `APPROVER1REMARKS` | VARCHAR(200) |  |  |  |  |
| 21 | `APPROVER2REMARKS` | VARCHAR(200) |  |  |  |  |
| 22 | `REJECTIONREASON` | VARCHAR(200) |  |  |  |  |
| 23 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 24 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 25 | `PROJECTSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SALESORDERLINEPROJECT.COMPANYCODE = COMPANY.CODE` |
| `PROJECT_PROJECT` | `COMPANYCODE`, `PROJECTCODE` | [`PROJECT`](../CORE_MASTER/PROJECT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESORDERLINEPROJECT.COMPANYCODE = PROJECT.COMPANYCODE AND SALESORDERLINEPROJECT.PROJECTCODE = PROJECT.CODE` |
| `SALESORDERLINE_SOLINE` | `COMPANYCODE`, `SOLINESALESORDERCOUNTERCODE`, `SOLINESALESORDERCODE`, `SOLINEORDERLINE`, `SOLINEORDERSUBLINE`, `SOLINECOMPONENTORDERLINE` | [`SALESORDERLINE`](../SALES/SALESORDERLINE.md) | `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE` | RESTRICT | `SALESORDERLINEPROJECT.COMPANYCODE = SALESORDERLINE.SALESORDERCOMPANYCODE AND SALESORDERLINEPROJECT.SOLINESALESORDERCOUNTERCODE = SALESORDERLINE.SALESORDERCOUNTERCODE AND SALESORDERLINEPROJECT.SOLINESALESORDERCODE = SALESORDERLINE.SALESORDERCODE AND SALESORDERLINEPROJECT.SOLINEORDERLINE = SALESORDERLINE.ORDERLINE AND SALESORDERLINEPROJECT.SOLINEORDERSUBLINE = SALESORDERLINE.ORDERSUBLINE AND SALESORDERLINEPROJECT.SOLINECOMPONENTORDERLINE = SALESORDERLINE.COMPONENTORDERLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERLINEPROJECTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LINENO,
       t.COMPANYCODE,
       t.SOLINESALESORDERCOUNTERCODE,
       t.SOLINESALESORDERCODE,
       t.SOLINEORDERLINE,
       t.SOLINEORDERSUBLINE,
       t.SOLINECOMPONENTORDERLINE,
       t.PROJECTCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03
FROM   DB2ADMIN.SALESORDERLINEPROJECT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
