# DB2ADMIN.MEDICAL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `MEDICALTYPE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 158091

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `MEDICALTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | BIGINT | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `DRNAME` | CHAR(30) |  |  |  |  |
| 4 | `MEDICALSTORE` | CHAR(30) |  |  |  |  |
| 5 | `HSPNAME` | CHAR(30) |  |  |  |  |
| 6 | `DRDEGREE` | CHAR(20) |  |  |  |  |
| 7 | `GOVAPROVED` | INTEGER | NOT NULL |  |  |  |
| 8 | `LICENCENO` | CHAR(25) | NOT NULL |  |  |  |
| 9 | `MEDICALADDR` | CHAR(100) |  |  |  |  |
| 10 | `PHONE` | CHAR(15) | NOT NULL |  |  |  |
| 11 | `FAX` | CHAR(15) |  |  |  |  |
| 12 | `EMAIL` | CHAR(30) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MEDICAL.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `MEDICAL_DMSTORE` | [`MEDICALBILLDETAIL`](../HR/MEDICALBILLDETAIL.md) | `MEDICALBILLHEADERCOMPANYCODE`, `MEDICALTYPE`, `DMSTORECODE` | `MEDICALBILLDETAIL.MEDICALBILLHEADERCOMPANYCODE = MEDICAL.COMPANYCODE AND MEDICALBILLDETAIL.MEDICALTYPE = MEDICAL.MEDICALTYPE AND MEDICALBILLDETAIL.DMSTORECODE = MEDICAL.CODE` |

## Indexes

- `MEDICALUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.MEDICALTYPE,
       t.CODE,
       t.DRNAME,
       t.MEDICALSTORE,
       t.HSPNAME,
       t.DRDEGREE,
       t.GOVAPROVED,
       t.LICENCENO,
       t.MEDICALADDR,
       t.PHONE,
       t.FAX
FROM   DB2ADMIN.MEDICAL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
