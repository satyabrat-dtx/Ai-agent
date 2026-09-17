# DB2ADMIN.RULEENTITYATTRIBUTE

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `TEMPLATECODE`, `ENTITYCODE`, `IDENTIFIER`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42173

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `ENTITYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `IDENTIFIER` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 4 | `ADENTITYNAME` | CHAR(50) |  | FK | foreign_key |  |
| 5 | `ADDATANAME` | CHAR(50) |  |  |  |  |
| 6 | `ADFIELDNAME` | VARCHAR(120) |  |  |  |  |
| 7 | `ABSUIXMLABSUIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 8 | `ABSUIXMLABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 9 | `ABSUIXMLNAME` | VARCHAR(120) |  |  |  |  |
| 10 | `LABEL` | CHAR(120) |  |  |  |  |
| 11 | `SEQUENCE` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `REALREFERENCED` | VARCHAR(100) |  |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADENTITY_ADENTITY` | `ADENTITYNAME` | [`ADENTITY`](../LOCALIZATION/ADENTITY.md) | `NAME` | RESTRICT | `RULEENTITYATTRIBUTE.ADENTITYNAME = ADENTITY.NAME` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RULEENTITYATTRIBUTE.COMPANYCODE = COMPANY.CODE` |
| `RULEENTITY_ENTITY` | `ENTITYCODE` | [`RULEENTITY`](../PLATFORM/RULEENTITY.md) | `CODE` | RESTRICT | `RULEENTITYATTRIBUTE.ENTITYCODE = RULEENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RULEENTITYATTRIBUTEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ENTITYCODE,
       t.IDENTIFIER,
       t.ADENTITYNAME,
       t.ADDATANAME,
       t.ADFIELDNAME,
       t.ABSUIXMLABSUIXMLPATH,
       t.ABSUIXMLABSUIXMLNAME,
       t.ABSUIXMLNAME,
       t.LABEL,
       t.SEQUENCE
FROM   DB2ADMIN.RULEENTITYATTRIBUTE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
