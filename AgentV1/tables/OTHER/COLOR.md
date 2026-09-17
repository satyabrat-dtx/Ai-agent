# DB2ADMIN.COLOR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COLORFOLDERCOMPANYCODE`, `COLORFOLDERCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 104624

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COLORFOLDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COLORFOLDERCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `COLORRGB` | CHAR(16) |  |  |  |  |
| 7 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `COLORTONECODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COLORFOLDER_COLOR` | `COLORFOLDERCOMPANYCODE`, `COLORFOLDERCODE` | [`COLORFOLDER`](../OTHER/COLORFOLDER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COLOR.COLORFOLDERCOMPANYCODE = COLORFOLDER.COMPANYCODE AND COLOR.COLORFOLDERCODE = COLORFOLDER.CODE` |
| `COLORTONE_COLORTONE` | `COLORFOLDERCOMPANYCODE`, `COLORTONECODE` | [`COLORTONE`](../OTHER/COLORTONE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COLOR.COLORFOLDERCOMPANYCODE = COLORTONE.COMPANYCODE AND COLOR.COLORTONECODE = COLORTONE.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `COLOR.OWNINGCOMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `COLOR_APPROVALREQUESTCOLORLINK` | [`APPROVALREQUESTCOLOR`](../OTHER/APPROVALREQUESTCOLOR.md) | `COLORCOLORFOLDERCOMPANYCODE`, `COLORCOLORFOLDERCODE`, `COLORCODE` | `APPROVALREQUESTCOLOR.COLORCOLORFOLDERCOMPANYCODE = COLOR.COLORFOLDERCOMPANYCODE AND APPROVALREQUESTCOLOR.COLORCOLORFOLDERCODE = COLOR.COLORFOLDERCODE AND APPROVALREQUESTCOLOR.COLORCODE = COLOR.CODE` |

## Indexes

- `COLORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COLORFOLDERCOMPANYCODE,
       t.COLORFOLDERCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COLORRGB,
       t.SEQUENCE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.COLOR t
FETCH FIRST 100 ROWS ONLY;
```
