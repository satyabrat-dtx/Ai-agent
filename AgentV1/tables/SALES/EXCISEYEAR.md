# DB2ADMIN.EXCISEYEAR

- **Module**: `SALES` (low confidence — FK neighbourhood: 2 of 3 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 35
- **Primary key**: `COMPANYCODE`, `REGNO`, `CODE`
- **FK degree**: referenced by 5 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121764

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `REGNO` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(4) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `EFFECTIVEFROMDATE` | DATE | NOT NULL |  |  |  |
| 7 | `EFFECTIVETODATE` | DATE | NOT NULL |  |  |  |
| 8 | `RG23IIINPUTNCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 9 | `IASTARTINGSEQUENCE` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 10 | `ICSTARTINGSEQUENCE` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 11 | `IIASTARTINGSEQUENCE` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 12 | `IICSTARTINGSEQUENCE` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 13 | `IARUNNINGSEQUENCE` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 14 | `ICRUNNINGSEQUENCE` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 15 | `IIARUNNINGSEQUENCE` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 16 | `IICRUNNINGSEQUENCE` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 17 | `IASTARTINGSEQFORST` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 18 | `ICSTARTINGSEQFORST` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 19 | `IARUNNINGSEQFORST` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 20 | `ICRUNNINGSEQFORST` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 21 | `IICSTARTINGSEQFORNY` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 22 | `IICRUNNINGSEQFORNY` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 23 | `PLAENTRYSTARTINGSEQFORNY` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 24 | `PLAENTRYRUNNINGSEQFORNY` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 25 | `REBATESTARTINGSEQ` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 26 | `REBATERUNNINGSEQ` | DECIMAL(9,0) | NOT NULL |  |  |  |
| 27 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 28 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 29 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 30 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 31 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 32 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 33 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 34 | `EINVOICEFISCALYEAR` | VARCHAR(80) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EXCISEYEAR.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 5

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EXCISEYEAR_EXCISEYEAR` | [`AR3`](../SALES/AR3.md) | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE` | `AR3.COMPANYCODE = EXCISEYEAR.COMPANYCODE AND AR3.EXCISEYEARREGNO = EXCISEYEAR.REGNO AND AR3.EXCISEYEARCODE = EXCISEYEAR.CODE` |
| `EXCISEYEAR_EXCISEYEAR` | [`AR4`](../SALES/AR4.md) | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE` | `AR4.COMPANYCODE = EXCISEYEAR.COMPANYCODE AND AR4.EXCISEYEARREGNO = EXCISEYEAR.REGNO AND AR4.EXCISEYEARCODE = EXCISEYEAR.CODE` |
| `EXCISEYEAR_EXCISEYEAR` | [`CENVATCREDITREGISTERREPORT`](../OTHER/CENVATCREDITREGISTERREPORT.md) | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE` | `CENVATCREDITREGISTERREPORT.COMPANYCODE = EXCISEYEAR.COMPANYCODE AND CENVATCREDITREGISTERREPORT.EXCISEYEARREGNO = EXCISEYEAR.REGNO AND CENVATCREDITREGISTERREPORT.EXCISEYEARCODE = EXCISEYEAR.CODE` |
| `EXCISEYEAR_EXCISEYEAR` | [`RG1TRANSACTION`](../QUALITY/RG1TRANSACTION.md) | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE` | `RG1TRANSACTION.COMPANYCODE = EXCISEYEAR.COMPANYCODE AND RG1TRANSACTION.EXCISEYEARREGNO = EXCISEYEAR.REGNO AND RG1TRANSACTION.EXCISEYEARCODE = EXCISEYEAR.CODE` |
| `EXCISEYEAR_EXCISEYEAR` | [`RG23PARTIREPORT`](../OTHER/RG23PARTIREPORT.md) | `COMPANYCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE` | `RG23PARTIREPORT.COMPANYCODE = EXCISEYEAR.COMPANYCODE AND RG23PARTIREPORT.EXCISEYEARREGNO = EXCISEYEAR.REGNO AND RG23PARTIREPORT.EXCISEYEARCODE = EXCISEYEAR.CODE` |

## Indexes

- `EXCISEYEARUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.REGNO,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.RG23IIINPUTNCAPITAL,
       t.IASTARTINGSEQUENCE,
       t.ICSTARTINGSEQUENCE,
       t.IIASTARTINGSEQUENCE
FROM   DB2ADMIN.EXCISEYEAR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
