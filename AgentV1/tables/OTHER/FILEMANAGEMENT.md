# DB2ADMIN.FILEMANAGEMENT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `COMPANYCODE`, `MODULENAMEICSTABLECODE`, `MODULENAMECODE`, `FILETYPE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 156704

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `MODULENAMEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MODULENAMECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `FILETYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `CODE` | CHAR(6) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `KEYBASEDFOLDER` | INTEGER | NOT NULL |  |  |  |
| 9 | `FILETYPEBASEDFOLDER` | INTEGER | NOT NULL |  |  |  |
| 10 | `KEYAPPENDEDFILE` | INTEGER | NOT NULL |  |  |  |
| 11 | `SUBKEYAPPENDEDFILE` | INTEGER | NOT NULL |  |  |  |
| 12 | `DIRECTORYPATH` | VARCHAR(250) |  |  |  |  |
| 13 | `FILEEXTENSION` | VARCHAR(250) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `RELATIVEPATH` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FILEMANAGEMENT.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_MODULENAME` | `COMPANYCODE`, `MODULENAMEICSTABLECODE`, `MODULENAMECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `FILEMANAGEMENT.COMPANYCODE = ICSENTITY.COMPANYCODE AND FILEMANAGEMENT.MODULENAMEICSTABLECODE = ICSENTITY.ICSTABLECODE AND FILEMANAGEMENT.MODULENAMECODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FILEMANAGEMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.MODULENAMEICSTABLECODE,
       t.MODULENAMECODE,
       t.FILETYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.KEYBASEDFOLDER,
       t.FILETYPEBASEDFOLDER,
       t.KEYAPPENDEDFILE,
       t.SUBKEYAPPENDEDFILE
FROM   DB2ADMIN.FILEMANAGEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
