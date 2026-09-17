# DB2ADMIN.ABSUIXMLBUTTONCUSTOMVALUE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `ABSUIXMLBUTTONABSUIXMLPATH`, `ABSUIXMLBUTTONABSUIXMLNAME`, `ABSUIXMLBUTTONNAME`, `ABSUIXMLBUTTONFORM`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34470

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSUIXMLBUTTONABSUIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `ABSUIXMLBUTTONABSUIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `ABSUIXMLBUTTONNAME` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 3 | `ABSUIXMLBUTTONFORM` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 5 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `HIDDENONVIEW` | CHAR(1) |  |  |  |  |
| 7 | `HIDDENONCREATE` | CHAR(1) |  |  |  |  |
| 8 | `HIDDENONMODIFY` | CHAR(1) |  |  |  |  |
| 9 | `SHOWONPOPUP` | CHAR(1) |  |  |  |  |
| 10 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 11 | `EVENTMASK` | INTEGER | NOT NULL |  |  |  |
| 12 | `EVENTKEY` | INTEGER | NOT NULL |  |  |  |
| 13 | `CUSTOMCSS` | CHAR(50) |  |  |  |  |
| 14 | `REFERENCED` | VARCHAR(100) |  |  |  |  |
| 15 | `ACTIONTODO` | VARCHAR(250) |  |  |  |  |
| 16 | `PARAMETERS` | VARCHAR(1500) |  |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `ICONCLS` | CHAR(30) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSUIXMLBUTTONCUSTOMVALUEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSUIXMLBUTTONABSUIXMLPATH,
       t.ABSUIXMLBUTTONABSUIXMLNAME,
       t.ABSUIXMLBUTTONNAME,
       t.ABSUIXMLBUTTONFORM,
       t.USERUSERID,
       t.COMPANYCODE,
       t.HIDDENONVIEW,
       t.HIDDENONCREATE,
       t.HIDDENONMODIFY,
       t.SHOWONPOPUP,
       t.SEQUENCE,
       t.EVENTMASK
FROM   DB2ADMIN.ABSUIXMLBUTTONCUSTOMVALUE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
