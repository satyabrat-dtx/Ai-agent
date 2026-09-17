# DB2ADMIN.STOCKDEALLOCATEFROMPROJECT

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `NUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193993

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `PROJECTCODE` | CHAR(20) |  | FK | foreign_key |  |
| 3 | `NONUSABLE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `BASEPRIMARYUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `BASEPRIMARYQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 17 | `PACKAGINGCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `PACKAGINGQUANTITYUNIT` | DECIMAL(15,5) |  |  |  |  |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `STOCKDEALLOCATEFROMPROJECT.COMPANYCODE = COMPANY.CODE` |
| `PROJECT_PROJECT` | `COMPANYCODE`, `PROJECTCODE` | [`PROJECT`](../CORE_MASTER/PROJECT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `STOCKDEALLOCATEFROMPROJECT.COMPANYCODE = PROJECT.COMPANYCODE AND STOCKDEALLOCATEFROMPROJECT.PROJECTCODE = PROJECT.CODE` |
| `UNITOFMEASURE_BASEPRIMARYUNIT` | `BASEPRIMARYUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `STOCKDEALLOCATEFROMPROJECT.BASEPRIMARYUNITCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_PACKAGING` | `PACKAGINGCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `STOCKDEALLOCATEFROMPROJECT.PACKAGINGCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKDEALLOCATEFROMPROJECTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NUMBERID,
       t.PROJECTCODE,
       t.NONUSABLE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.STOCKDEALLOCATEFROMPROJECT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
