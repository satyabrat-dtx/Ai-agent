# DB2ADMIN.SEPAMANDATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `MANDATEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 104538

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `MANDATEID` | CHAR(40) | NOT NULL | PK | primary_key |  |
| 2 | `COLLECTIONTYPE` | CHAR(1) |  |  |  |  |
| 3 | `DATESIGNED` | DATE | NOT NULL |  |  |  |
| 4 | `INITIALDATE` | DATE | NOT NULL |  |  |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `FINALDATE` | DATE |  |  |  |  |
| 9 | `LASTUSAGEDATE` | DATE |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SEPAMANDATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SEPAMANDATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.MANDATEID,
       t.COLLECTIONTYPE,
       t.DATESIGNED,
       t.INITIALDATE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.FINALDATE,
       t.LASTUSAGEDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.SEPAMANDATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
