# DB2ADMIN.NETEINVOICECUSTOMIZEDOPTIONS

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 238564

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PORTAL` | CHAR(1) |  |  |  |  |
| 2 | `WEBTELCDKEY` | CHAR(100) |  |  |  |  |
| 3 | `WEBTELINVUSERNAME` | CHAR(100) |  |  |  |  |
| 4 | `WEBTELINVPASSWORD` | CHAR(100) |  |  |  |  |
| 5 | `WEBTELINRURL` | VARCHAR(500) |  |  |  |  |
| 6 | `WEBTELCANCELURL` | VARCHAR(500) |  |  |  |  |
| 7 | `WEBTELEWAYBILLURL` | VARCHAR(500) |  |  |  |  |
| 8 | `WEBTELPDFURL` | VARCHAR(500) |  |  |  |  |
| 9 | `IRISUSERNAME` | CHAR(100) |  |  |  |  |
| 10 | `IRISPASSWORD` | CHAR(100) |  |  |  |  |
| 11 | `IRISINRURL` | VARCHAR(500) |  |  |  |  |
| 12 | `IRISCANCLEURL` | VARCHAR(500) |  |  |  |  |
| 13 | `IRISCANCLEEWBURL` | VARCHAR(500) |  |  |  |  |
| 14 | `IRISEWAYBILLURL` | VARCHAR(500) |  |  |  |  |
| 15 | `IRISLOGINURL` | VARCHAR(500) |  |  |  |  |
| 16 | `B2CLVALUE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETEINVCUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PORTAL,
       t.WEBTELCDKEY,
       t.WEBTELINVUSERNAME,
       t.WEBTELINVPASSWORD,
       t.WEBTELINRURL,
       t.WEBTELCANCELURL,
       t.WEBTELEWAYBILLURL,
       t.WEBTELPDFURL,
       t.IRISUSERNAME,
       t.IRISPASSWORD,
       t.IRISINRURL
FROM   DB2ADMIN.NETEINVOICECUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
