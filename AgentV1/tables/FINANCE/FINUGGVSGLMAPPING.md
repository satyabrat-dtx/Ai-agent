# DB2ADMIN.FINUGGVSGLMAPPING

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `UGGUSERGENERICGROUPTYPECODE`, `UGGCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 175709

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `UGGUGENGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `UGGUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `UGGCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `GLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `GLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINUGGVSGLMAPPING.COMPANYCODE = COMPANY.CODE` |
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINUGGVSGLMAPPING.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND FINUGGVSGLMAPPING.GLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINUGGVSGLMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.UGGUGENGROUPTYPECOMPANYCODE,
       t.UGGUSERGENERICGROUPTYPECODE,
       t.UGGCODE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.FINUGGVSGLMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
