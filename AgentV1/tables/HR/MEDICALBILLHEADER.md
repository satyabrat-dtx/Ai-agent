# DB2ADMIN.MEDICALBILLHEADER

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `YEAR`, `EMPLOYEENO`, `ACCIDENTNOCODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 167653

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `YEAR` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 2 | `ACCIDENTNOCODE` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EMPLOYEENO` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 4 | `FLAG` | INTEGER | NOT NULL |  |  |  |
| 5 | `MRRECEIVED` | INTEGER | NOT NULL |  |  |  |
| 6 | `RECDATE` | DATE |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACCINTIMATION_ACCIDENTNO` | `COMPANYCODE`, `ACCIDENTNOCODE` | [`ACCINTIMATION`](../HR/ACCINTIMATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MEDICALBILLHEADER.COMPANYCODE = ACCINTIMATION.COMPANYCODE AND MEDICALBILLHEADER.ACCIDENTNOCODE = ACCINTIMATION.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MEDICALBILLHEADER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `MEDICALBILLHEADER_DETAILS` | [`MEDICALBILLDETAIL`](../HR/MEDICALBILLDETAIL.md) | `MEDICALBILLHEADERCOMPANYCODE`, `MEDICALBILLHEADERYEAR`, `MEDICALBILLHEADEREMPLOYEENO`, `MEDICALBIHEADERACCIDENTNOCODE` | `MEDICALBILLDETAIL.MEDICALBILLHEADERCOMPANYCODE = MEDICALBILLHEADER.COMPANYCODE AND MEDICALBILLDETAIL.MEDICALBILLHEADERYEAR = MEDICALBILLHEADER.YEAR AND MEDICALBILLDETAIL.MEDICALBILLHEADEREMPLOYEENO = MEDICALBILLHEADER.EMPLOYEENO AND MEDICALBILLDETAIL.MEDICALBIHEADERACCIDENTNOCODE = MEDICALBILLHEADER.ACCIDENTNOCODE` |

## Indexes

- `MEDICALBILLHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.YEAR,
       t.ACCIDENTNOCODE,
       t.EMPLOYEENO,
       t.FLAG,
       t.MRRECEIVED,
       t.RECDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.MEDICALBILLHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
