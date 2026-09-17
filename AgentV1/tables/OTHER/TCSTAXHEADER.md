# DB2ADMIN.TCSTAXHEADER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `NUMBERID`, `COMPANYCODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221171

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISION` | CHAR(5) |  |  |  |  |
| 3 | `TCSTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 5 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 6 | `TYPEOFBUSINESS` | CHAR(2) |  |  |  |  |
| 7 | `CAPVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TCSTAXHEADER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TCSTAXHEADER_DETAIL` | [`TCSTAXDETAIL`](../OTHER/TCSTAXDETAIL.md) | `TCSTAXHEADERNUMBERID`, `TCSTAXHEADERCOMPANYCODE` | `TCSTAXDETAIL.TCSTAXHEADERNUMBERID = TCSTAXHEADER.NUMBERID AND TCSTAXDETAIL.TCSTAXHEADERCOMPANYCODE = TCSTAXHEADER.COMPANYCODE` |

## Indexes

- `TCSTAXHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.NUMBERID,
       t.COMPANYCODE,
       t.DIVISION,
       t.TCSTYPE,
       t.FROMDATE,
       t.TODATE,
       t.TYPEOFBUSINESS,
       t.CAPVALUE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.TCSTAXHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
