# DB2ADMIN.APPCATALOGCONFIG

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114145

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CATALOGSEQUENCE` | CHAR(120) | NOT NULL |  |  |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPESHORTDESC` | VARCHAR(40) |  |  |  |  |
| 5 | `ITEMTYPELONGDESC` | VARCHAR(100) |  |  |  |  |
| 6 | `ITEMTYPESUBCODESEQUENCE` | CHAR(30) | NOT NULL |  |  |  |
| 7 | `ITEMTYPEROWMATRIX` | INTEGER | NOT NULL |  |  |  |
| 8 | `ITEMTYPECOLMATRIX` | INTEGER | NOT NULL |  |  |  |
| 9 | `SUBCODE01DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 10 | `SUBCODE02DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 11 | `SUBCODE03DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 12 | `SUBCODE04DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 13 | `SUBCODE05DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 14 | `SUBCODE06DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 15 | `SUBCODE07DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 16 | `SUBCODE08DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 17 | `SUBCODE09DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 18 | `SUBCODE10DESCRIPTION` | VARCHAR(60) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPCATALOGCONFIGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CATALOGSEQUENCE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.ITEMTYPESHORTDESC,
       t.ITEMTYPELONGDESC,
       t.ITEMTYPESUBCODESEQUENCE,
       t.ITEMTYPEROWMATRIX,
       t.ITEMTYPECOLMATRIX,
       t.SUBCODE01DESCRIPTION,
       t.SUBCODE02DESCRIPTION,
       t.SUBCODE03DESCRIPTION
FROM   DB2ADMIN.APPCATALOGCONFIG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
