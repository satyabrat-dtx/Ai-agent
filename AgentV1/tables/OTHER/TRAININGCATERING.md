# DB2ADMIN.TRAININGCATERING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `CATERINGCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 161396

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CATERINGCODE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 2 | `CATERINGNAME` | CHAR(25) | NOT NULL |  |  |  |
| 3 | `ADDRESS` | VARCHAR(200) |  |  |  |  |
| 4 | `CITY` | VARCHAR(200) |  |  |  |  |
| 5 | `STATE` | VARCHAR(200) |  |  |  |  |
| 6 | `COUNTRY` | VARCHAR(200) |  |  |  |  |
| 7 | `PRIMARYPHONENO` | CHAR(12) | NOT NULL |  |  |  |
| 8 | `MOBILENO` | CHAR(12) |  |  |  |  |
| 9 | `FAXNUMBER` | CHAR(12) |  |  |  |  |
| 10 | `EMAILID` | CHAR(25) |  |  |  |  |
| 11 | `BANKNAME` | CHAR(25) |  |  |  |  |
| 12 | `ACCOUNTNUMBER` | CHAR(12) |  |  |  |  |
| 13 | `PANNO` | CHAR(30) |  |  |  |  |
| 14 | `MICR` | CHAR(30) |  |  |  |  |
| 15 | `IFSC` | CHAR(30) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRAININGCATERING.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TRAININGCATERINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CATERINGCODE,
       t.CATERINGNAME,
       t.ADDRESS,
       t.CITY,
       t.STATE,
       t.COUNTRY,
       t.PRIMARYPHONENO,
       t.MOBILENO,
       t.FAXNUMBER,
       t.EMAILID,
       t.BANKNAME
FROM   DB2ADMIN.TRAININGCATERING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
