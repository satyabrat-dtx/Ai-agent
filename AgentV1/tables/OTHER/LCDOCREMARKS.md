# DB2ADMIN.LCDOCREMARKS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 38
- **Primary key**: `COMPANYCODE`, `LCNO`, `LCDATE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 139912

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LCNO` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 2 | `LCDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `BOEREMARKS` | VARCHAR(1000) |  |  |  |  |
| 4 | `BANKCOVERNOTEREMARKS` | VARCHAR(1000) |  |  |  |  |
| 5 | `PRESHIPMENTINSPECTIONREMARKS` | VARCHAR(1000) |  |  |  |  |
| 6 | `SHIPMENTADVICEREMARKS` | VARCHAR(1000) |  |  |  |  |
| 7 | `COOREMARKS` | VARCHAR(1000) |  |  |  |  |
| 8 | `INSURANCEINTIMATIONREMARKS` | VARCHAR(1000) |  |  |  |  |
| 9 | `COMMERCIALINVOICEREMARKS` | VARCHAR(1000) |  |  |  |  |
| 10 | `PACKINGLISTREMARKS` | VARCHAR(1000) |  |  |  |  |
| 11 | `BC1REMARKS` | VARCHAR(1000) |  |  |  |  |
| 12 | `BC2REMARKS` | VARCHAR(1000) |  |  |  |  |
| 13 | `BC3REMARKS` | VARCHAR(1000) |  |  |  |  |
| 14 | `BC4REMARKS` | VARCHAR(1000) |  |  |  |  |
| 15 | `BC5REMARKS` | VARCHAR(1000) |  |  |  |  |
| 16 | `BC6REMARKS` | VARCHAR(1000) |  |  |  |  |
| 17 | `BC7REMARKS` | VARCHAR(1000) |  |  |  |  |
| 18 | `BLIREMARKS` | VARCHAR(1000) |  |  |  |  |
| 19 | `BC8REMARKS` | VARCHAR(1000) |  |  |  |  |
| 20 | `BC9REMARKS` | VARCHAR(1000) |  |  |  |  |
| 21 | `BC10REMARKS` | VARCHAR(1000) |  |  |  |  |
| 22 | `EX1REMARKS` | VARCHAR(1000) |  |  |  |  |
| 23 | `EX2REMARKS` | VARCHAR(1000) |  |  |  |  |
| 24 | `EX3REMARKS` | VARCHAR(1000) |  |  |  |  |
| 25 | `EX4REMARKS` | VARCHAR(1000) |  |  |  |  |
| 26 | `EX5REMARKS` | VARCHAR(1000) |  |  |  |  |
| 27 | `GCCIREMARKS` | VARCHAR(1000) |  |  |  |  |
| 28 | `TCREMARKS` | VARCHAR(1000) |  |  |  |  |
| 29 | `GSPREMARKS` | VARCHAR(1000) |  |  |  |  |
| 30 | `PARTYCOVERINGREMARKS` | VARCHAR(1000) |  |  |  |  |
| 31 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 32 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 33 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 34 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 35 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 36 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LCDOCREMARKS.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LCDOCREMARKSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LCNO,
       t.LCDATE,
       t.BOEREMARKS,
       t.BANKCOVERNOTEREMARKS,
       t.PRESHIPMENTINSPECTIONREMARKS,
       t.SHIPMENTADVICEREMARKS,
       t.COOREMARKS,
       t.INSURANCEINTIMATIONREMARKS,
       t.COMMERCIALINVOICEREMARKS,
       t.PACKINGLISTREMARKS,
       t.BC1REMARKS
FROM   DB2ADMIN.LCDOCREMARKS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
