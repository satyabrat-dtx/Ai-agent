# DB2ADMIN.EXPORTENTITY

- **Module**: `PDM` (low confidence — FK neighbourhood: 1 of 1 related tables are PDM)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ENVIRONMENTCODE`, `ENTITYNAME`, `COMPANYCODE`, `TEMPLATECODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 27853

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ENVIRONMENTCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ENTITYNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `TEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EXPORTENVIRONMENT_ENVIRONMENT` | `ENVIRONMENTCODE` | [`EXPORTENVIRONMENT`](../PDM/EXPORTENVIRONMENT.md) | `CODE` | RESTRICT | `EXPORTENTITY.ENVIRONMENTCODE = EXPORTENVIRONMENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXPORTENTITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ENVIRONMENTCODE,
       t.ENTITYNAME,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ITEMTYPECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ITEMTYPECOMPANYCODE,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.EXPORTENTITY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
