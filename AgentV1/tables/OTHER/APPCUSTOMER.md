# DB2ADMIN.APPCUSTOMER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `CUSTOMERID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 114199

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CUSTOMERID` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 2 | `CUSTOMERNAME` | VARCHAR(100) |  |  |  |  |
| 3 | `CURRENCYCODE` | CHAR(10) |  |  |  |  |
| 4 | `CREATEDBYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `CUSTOMERCARDIMAGE` | BLOB(1000000) |  |  |  |  |
| 6 | `CUSTOMERCARDMIMETYPE` | CHAR(10) |  |  |  |  |
| 7 | `ADDRESSEE` | VARCHAR(100) |  |  |  |  |
| 8 | `ADDRESSLINE1` | VARCHAR(100) |  |  |  |  |
| 9 | `ADDRESSLINE2` | VARCHAR(100) |  |  |  |  |
| 10 | `ADDRESSLINE3` | VARCHAR(100) |  |  |  |  |
| 11 | `ADDRESSLINE4` | VARCHAR(100) |  |  |  |  |
| 12 | `ADDRESSLINE5` | VARCHAR(100) |  |  |  |  |
| 13 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 14 | `TOWN` | VARCHAR(100) |  |  |  |  |
| 15 | `COUNTRYNAME` | VARCHAR(100) |  |  |  |  |
| 16 | `DISTRICT` | VARCHAR(100) |  |  |  |  |
| 17 | `ADDRESSPHONENUMBER` | VARCHAR(40) |  |  |  |  |
| 18 | `ADDRESSFAXNUMBER` | VARCHAR(40) |  |  |  |  |
| 19 | `EMAILADDRESS` | VARCHAR(100) |  |  |  |  |
| 20 | `DIRTYFLAG` | SMALLINT | NOT NULL |  |  |  |
| 21 | `ORDERPARTNERUPDATED` | SMALLINT | NOT NULL |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AGENT_CREATEDBY` | `COMPANYCODE`, `CREATEDBYCODE` | [`AGENT`](../CORE_MASTER/AGENT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `APPCUSTOMER.COMPANYCODE = AGENT.COMPANYCODE AND APPCUSTOMER.CREATEDBYCODE = AGENT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPCUSTOMERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CUSTOMERID,
       t.CUSTOMERNAME,
       t.CURRENCYCODE,
       t.CREATEDBYCODE,
       t.CUSTOMERCARDIMAGE,
       t.CUSTOMERCARDMIMETYPE,
       t.ADDRESSEE,
       t.ADDRESSLINE1,
       t.ADDRESSLINE2,
       t.ADDRESSLINE3,
       t.ADDRESSLINE4
FROM   DB2ADMIN.APPCUSTOMER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
